
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import motor.motor_asyncio
import re

app = FastAPI()

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.interview_db
users_collection = db.users

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users")
async def create_user(user: UserCreate):
    try:
        if len(user.name) < 3 or not re.match(r"^[A-Za-z ]+$", user.name):
            raise HTTPException(status_code=400, detail="Invalid name.")
        
        if "@" not in user.email:
            raise HTTPException(status_code=400, detail="Invalid email format")
        
        if user.age < 18:
            raise HTTPException(status_code=400, detail="Invalid age. Must be 18 or older")
        if user.age < 25:
            badge = "Young Explorer"
        elif 25 <= user.age <= 50:
            badge = "Professional"
        else:
            badge = "Veteran"

        if user.email.endswith("@company.com"):
            badge = "VIP" 
        existing_user = await users_collection.find_one({"email": user.email})
        if existing_user:
            raise HTTPException(status_code=409, detail="User already exists")

        new_user = {
            "name": user.name,
            "email": user.email,
            "age": user.age,
            "badge": badge,
            "createdAt": db.command("serverStatus")["localTime"]
        }

        result = await users_collection.insert_one(new_user)
        if not result.inserted_id:
            raise HTTPException(status_code=500, detail="Failed to create user")

        return {
            "message": "User created successfully",
            "userId": str(result.inserted_id),
            "badge": badge
        }

    except HTTPException:
        raise  
    except Exception as e:
        print("Unhandled error:", e)
        raise HTTPException(status_code=500, detail="Internal server error")
