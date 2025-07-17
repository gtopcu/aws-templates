import boto3
from botocore.exceptions import ClientError
import json
from typing import Dict, List, Set, Tuple
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class DynamoDBTableSync:

    def __init__(self, aws_region='us-east-1', profile_name=None):
        """
        Initialize the DynamoDB client
        
        Args:
            aws_region (str): AWS region where tables are located
            profile_name (str): AWS profile name (optional)
        """
        if profile_name:
            session = boto3.Session(profile_name=profile_name)
            self.dynamodb = session.resource('dynamodb', region_name=aws_region)
        else:
            self.dynamodb = boto3.resource('dynamodb', region_name=aws_region)
        
        self.client = self.dynamodb.meta.client
    
    def get_table_keys(self, table_name: str) -> Tuple[str, str]:
        """
        Get the primary key and sort key for a table
        
        Args:
            table_name (str): Name of the DynamoDB table
            
        Returns:
            Tuple[str, str]: Primary key name and sort key name (None if no sort key)
        """
        try:
            response = self.client.describe_table(TableName=table_name)
            key_schema = response['Table']['KeySchema']
            
            pk = None
            sk = None
            
            for key in key_schema:
                if key['KeyType'] == 'HASH':
                    pk = key['AttributeName']
                elif key['KeyType'] == 'RANGE':
                    sk = key['AttributeName']
            
            return pk, sk
            
        except ClientError as e:
            logger.error(f"Error describing table {table_name}: {e}")
            raise
    
    def scan_table_items(self, table_name: str) -> List[Dict]:
        """
        Scan all items from a DynamoDB table
        
        Args:
            table_name (str): Name of the DynamoDB table
            
        Returns:
            List[Dict]: List of all items in the table
        """
        table = self.dynamodb.Table(table_name)
        items = []
        
        try:
            response = table.scan()
            items.extend(response['Items'])
            
            # Handle pagination
            while 'LastEvaluatedKey' in response:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                items.extend(response['Items'])
                
            logger.info(f"Scanned {len(items)} items from table {table_name}")
            return items
            
        except ClientError as e:
            logger.error(f"Error scanning table {table_name}: {e}")
            raise
    
    def create_key_set(self, items: List[Dict], pk: str, sk: str = None) -> Set[Tuple]:
        """
        Create a set of keys from items for comparison
        
        Args:
            items (List[Dict]): List of DynamoDB items
            pk (str): Primary key attribute name
            sk (str): Sort key attribute name (optional)
            
        Returns:
            Set[Tuple]: Set of key tuples
        """
        keys = set()
        
        for item in items:
            if sk:
                key = (item[pk], item[sk])
            else:
                key = (item[pk],)
            keys.add(key)
        
        return keys
    
    def find_missing_items(self, source_items: List[Dict], target_keys: Set[Tuple], 
                          pk: str, sk: str = None) -> List[Dict]:
        """
        Find items in source that are missing in target
        
        Args:
            source_items (List[Dict]): Items from source table
            target_keys (Set[Tuple]): Set of keys from target table
            pk (str): Primary key attribute name
            sk (str): Sort key attribute name (optional)
            
        Returns:
            List[Dict]: Items that are missing in target table
        """
        missing_items = []
        
        for item in source_items:
            if sk:
                key = (item[pk], item[sk])
            else:
                key = (item[pk],)
            
            if key not in target_keys:
                missing_items.append(item)
        
        return missing_items
    
    def batch_write_items(self, table_name: str, items: List[Dict], batch_size: int = 25):
        """
        Write items to DynamoDB table in batches
        
        Args:
            table_name (str): Name of the target table
            items (List[Dict]): Items to write
            batch_size (int): Number of items per batch (max 25 for DynamoDB)
        """
        table = self.dynamodb.Table(table_name)
        
        for i in range(0, len(items), batch_size):
            batch = items[i:i + batch_size]
            
            try:
                with table.batch_writer() as batch_writer:
                    for item in batch:
                        batch_writer.put_item(Item=item)
                
                logger.info(f"Successfully wrote batch of {len(batch)} items to {table_name}")
                
            except ClientError as e:
                logger.error(f"Error writing batch to {table_name}: {e}")
                # Retry individual items in case of partial failure
                for item in batch:
                    try:
                        table.put_item(Item=item)
                        logger.info(f"Successfully wrote individual item to {table_name}")
                    except ClientError as item_error:
                        logger.error(f"Failed to write item {item}: {item_error}")
    
    def sync_tables(self, source_table: str, target_table: str, 
                   batch_size: int = 25, dry_run: bool = False) -> Dict:
        """
        Compare two tables and copy missing items from source to target
        
        Args:
            source_table (str): Name of the source table
            target_table (str): Name of the target table
            batch_size (int): Batch size for writing items
            dry_run (bool): If True, only show what would be copied without actually copying
            
        Returns:
            Dict: Summary of the sync operation
        """
        logger.info(f"Starting sync from {source_table} to {target_table}")
        
        # Get table schemas
        source_pk, source_sk = self.get_table_keys(source_table)
        target_pk, target_sk = self.get_table_keys(target_table)
        
        logger.info(f"Source table keys: PK={source_pk}, SK={source_sk}")
        logger.info(f"Target table keys: PK={target_pk}, SK={target_sk}")
        
        # Scan both tables
        logger.info("Scanning source table...")
        source_items = self.scan_table_items(source_table)
        
        logger.info("Scanning target table...")
        target_items = self.scan_table_items(target_table)
        
        # Create key sets for comparison
        target_keys = self.create_key_set(target_items, target_pk, target_sk)
        
        # Find missing items
        missing_items = self.find_missing_items(source_items, target_keys, source_pk, source_sk)
        
        result = {
            'source_table': source_table,
            'target_table': target_table,
            'source_item_count': len(source_items),
            'target_item_count': len(target_items),
            'missing_item_count': len(missing_items),
            'dry_run': dry_run
        }
        
        logger.info(f"Found {len(missing_items)} missing items in target table")
        
        if missing_items:
            if dry_run:
                logger.info("DRY RUN: Would copy the following items:")
                for item in missing_items[:5]:  # Show first 5 items
                    logger.info(f"  {json.dumps(item, default=str)}")
                if len(missing_items) > 5:
                    logger.info(f"  ... and {len(missing_items) - 5} more items")
            else:
                logger.info(f"Copying {len(missing_items)} items to target table...")
                self.batch_write_items(target_table, missing_items, batch_size)
                logger.info("Sync completed successfully!")
        else:
            logger.info("No missing items found. Tables are in sync!")
        
        return result

def main():
    """
    Main function to run the table sync
    """
    # Configuration
    SOURCE_TABLE = "your-source-table-name"
    TARGET_TABLE = "your-target-table-name"
    AWS_REGION = "us-east-1"
    AWS_PROFILE = None  # Set to your AWS profile name if needed
    BATCH_SIZE = 25
    DRY_RUN = True  # Set to False to actually copy items
    
    # Initialize the sync utility
    sync_util = DynamoDBTableSync(aws_region=AWS_REGION, profile_name=AWS_PROFILE)
    
    try:
        # Run the sync
        result = sync_util.sync_tables(
            source_table=SOURCE_TABLE,
            target_table=TARGET_TABLE,
            batch_size=BATCH_SIZE,
            dry_run=DRY_RUN
        )
        
        # Print summary
        print("\n" + "="*50)
        print("SYNC SUMMARY")
        print("="*50)
        print(f"Source table: {result['source_table']}")
        print(f"Target table: {result['target_table']}")
        print(f"Source items: {result['source_item_count']}")
        print(f"Target items: {result['target_item_count']}")
        print(f"Missing items: {result['missing_item_count']}")
        print(f"Dry run: {result['dry_run']}")
        
    except Exception as e:
        logger.error(f"Error during sync: {e}")
        raise

if __name__ == "__main__":
    main()