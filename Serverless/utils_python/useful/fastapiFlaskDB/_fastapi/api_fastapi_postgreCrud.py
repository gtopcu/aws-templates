"""
Generic FastAPI + SQLAlchemy CRUD REST API Generator
=================================================

This application automatically generates CRUD REST API endpoints for 
any PostgreSQL database table using FastAPI and SQLAlchemy.

Requirements:
- Python 3.7+
- FastAPI
- SQLAlchemy
- psycopg2-binary
- pydantic
- uvicorn

To install dependencies:
pip install fastapi sqlalchemy psycopg2-binary pydantic uvicorn python-dotenv

To run the application:
uvicorn main:app --reload
"""

import os
from typing import Any, Dict, List, Optional, Type, TypeVar, Generic
from fastapi import FastAPI, HTTPException, Depends, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, create_model
from sqlalchemy import create_engine, MetaData, Table, Column, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database connection
DB_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

# Create SQLAlchemy engine
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = MetaData()

# FastAPI app
app = FastAPI(title="Generic PostgreSQL CRUD API")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to dynamically create Pydantic models for a table
def create_pydantic_model(table_name: str, table: Table):
    fields = {}
    for column in table.columns:
        python_type = None
        if hasattr(column.type, "python_type"):
            python_type = column.type.python_type
        else:
            # Default to string if python_type is not available
            python_type = str
            
        # Make field optional if column is nullable or has default/autoincrement
        is_optional = column.nullable or column.default is not None or column.autoincrement
        if is_optional:
            fields[column.name] = (Optional[python_type], None)
        else:
            fields[column.name] = (python_type, ...)
    
    # Create base model for data validation
    model = create_model(
        f"{table_name.capitalize()}Base",
        **fields
    )
    
    # Create model for creation (might exclude autoincrement primary keys)
    create_fields = {k: v for k, v in fields.items() 
                    if not (table.primary_key.columns and 
                            k in [c.name for c in table.primary_key.columns] and 
                            any(col.autoincrement for col in table.primary_key.columns if col.name == k))}
    
    create_model_cls = create_model(
        f"{table_name.capitalize()}Create",
        **create_fields
    )
    
    # Create model for updates (all fields optional)
    update_fields = {k: (Optional[v[0]], None) for k, v in fields.items()}
    update_model_cls = create_model(
        f"{table_name.capitalize()}Update",
        **update_fields
    )
    
    return model, create_model_cls, update_model_cls

# Cache for table models
table_models = {}

# Function to get or create models for a table
def get_table_models(table_name: str, db: Session):
    if table_name in table_models:
        return table_models[table_name]
    
    # Check if table exists
    if not engine.dialect.has_table(engine.connect(), table_name):
        raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found")
    
    # Reflect table from database
    metadata.clear()
    table = Table(table_name, metadata, autoload_with=engine)
    
    # Create models
    base_model, create_model, update_model = create_pydantic_model(table_name, table)
    
    # Cache the models and table
    table_models[table_name] = (base_model, create_model, update_model, table)
    
    return table_models[table_name]

@app.get("/")
def read_root():
    """API root endpoint showing available tables"""
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    return {"available_tables": tables}

@app.get("/tables/{table_name}", response_model=List[Dict[str, Any]])
def read_all_items(
    table_name: str, 
    db: Session = Depends(get_db),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000)
):
    """Get all items from a specific table with pagination"""
    try:
        _, _, _, table = get_table_models(table_name, db)
        
        # Execute query
        query = db.query(table).offset(skip).limit(limit).all()
        
        # Convert to list of dictionaries
        result = []
        for row in query:
            item = {column.name: getattr(row, column.name) for column in table.columns}
            result.append(item)
        
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {str(e)}")

@app.get("/tables/{table_name}/{item_id}", response_model=Dict[str, Any])
def read_item(table_name: str, item_id: Any, db: Session = Depends(get_db)):
    """Get a specific item by primary key"""
    try:
        _, _, _, table = get_table_models(table_name, db)
        
        # Get primary key column
        pk_columns = [c for c in table.primary_key.columns]
        if not pk_columns:
            raise HTTPException(status_code=400, detail=f"Table '{table_name}' has no primary key")
        
        # For simplicity, we use the first PK column
        pk_column = pk_columns[0]
        
        # Try to convert item_id to the correct type
        try:
            if hasattr(pk_column.type, "python_type"):
                typed_id = pk_column.type.python_type(item_id)
            else:
                typed_id = item_id
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid ID format for {pk_column.name}")
        
        # Query for the item
        query = db.query(table).filter(pk_column == typed_id).first()
        
        if not query:
            raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
        
        # Convert to dictionary
        result = {column.name: getattr(query, column.name) for column in table.columns}
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching item: {str(e)}")

@app.post("/tables/{table_name}", response_model=Dict[str, Any])
def create_item(table_name: str, item_data: Dict[str, Any], db: Session = Depends(get_db)):
    """Create a new item in the specified table"""
    try:
        _, create_model, _, table = get_table_models(table_name, db)
        
        # Validate input data
        validated_data = create_model(**item_data).dict(exclude_unset=True)
        
        try:
            # Create a new row
            stmt = table.insert().values(**validated_data).returning(*table.columns)
            result = db.execute(stmt)
            db.commit()
            
            # Get the inserted row
            row = result.fetchone()
            
            if row:
                # Convert to dictionary
                result_dict = {column.name: getattr(row, column.name) for column in table.columns}
                return result_dict
            return validated_data
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=f"Database error: {str(e)}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating item: {str(e)}")

@app.put("/tables/{table_name}/{item_id}", response_model=Dict[str, Any])
def update_item(table_name: str, item_id: Any, item_data: Dict[str, Any], db: Session = Depends(get_db)):
    """Update an existing item in the specified table"""
    try:
        _, _, update_model, table = get_table_models(table_name, db)
        
        # Get primary key column
        pk_columns = [c for c in table.primary_key.columns]
        if not pk_columns:
            raise HTTPException(status_code=400, detail=f"Table '{table_name}' has no primary key")
        
        # For simplicity, we use the first PK column
        pk_column = pk_columns[0]
        
        # Try to convert item_id to the correct type
        try:
            if hasattr(pk_column.type, "python_type"):
                typed_id = pk_column.type.python_type(item_id)
            else:
                typed_id = item_id
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid ID format for {pk_column.name}")
        
        # Check if item exists
        existing_item = db.query(table).filter(pk_column == typed_id).first()
        if not existing_item:
            raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
        
        # Validate update data
        validated_data = update_model(**item_data).dict(exclude_unset=True)
        
        if not validated_data:
            return {column.name: getattr(existing_item, column.name) for column in table.columns}
        
        try:
            # Update the row
            stmt = table.update().where(pk_column == typed_id).values(**validated_data).returning(*table.columns)
            result = db.execute(stmt)
            db.commit()
            
            # Get the updated row
            row = result.fetchone()
            
            if row:
                # Convert to dictionary
                result_dict = {column.name: getattr(row, column.name) for column in table.columns}
                return result_dict
            
            # Fallback if returning is not supported
            updated_item = db.query(table).filter(pk_column == typed_id).first()
            return {column.name: getattr(updated_item, column.name) for column in table.columns}
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=f"Database error: {str(e)}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating item: {str(e)}")

@app.delete("/tables/{table_name}/{item_id}", response_model=Dict[str, str])
def delete_item(table_name: str, item_id: Any, db: Session = Depends(get_db)):
    """Delete an item from the specified table"""
    try:
        _, _, _, table = get_table_models(table_name, db)
        
        # Get primary key column
        pk_columns = [c for c in table.primary_key.columns]
        if not pk_columns:
            raise HTTPException(status_code=400, detail=f"Table '{table_name}' has no primary key")
        
        # For simplicity, we use the first PK column
        pk_column = pk_columns[0]
        
        # Try to convert item_id to the correct type
        try:
            if hasattr(pk_column.type, "python_type"):
                typed_id = pk_column.type.python_type(item_id)
            else:
                typed_id = item_id
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid ID format for {pk_column.name}")
        
        # Check if item exists
        existing_item = db.query(table).filter(pk_column == typed_id).first()
        if not existing_item:
            raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")
        
        try:
            # Delete the row
            stmt = table.delete().where(pk_column == typed_id)
            db.execute(stmt)
            db.commit()
            
            return {"message": f"Item with id {item_id} successfully deleted"}
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(status_code=400, detail=f"Database error: {str(e)}")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting item: {str(e)}")

@app.get("/tables/{table_name}/schema", response_model=Dict[str, Any])
def get_table_schema(table_name: str, db: Session = Depends(get_db)):
    """Get the schema of a specific table"""
    try:
        _, _, _, table = get_table_models(table_name, db)
        
        schema = {}
        for column in table.columns:
            col_info = {
                "type": str(column.type),
                "nullable": column.nullable,
                "primary_key": column.primary_key,
                "default": str(column.default) if column.default is not None else None,
                "autoincrement": column.autoincrement if hasattr(column, "autoincrement") else False,
            }
            schema[column.name] = col_info
            
        return {
            "table_name": table_name,
            "columns": schema,
            "primary_key": [c.name for c in table.primary_key.columns] if table.primary_key else []
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching schema: {str(e)}")

# Create a .env file template
with open(".env.example", "w") as f:
    f.write("""# Database connection string
DATABASE_URL=postgresql://user:password@localhost/dbname
""")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)