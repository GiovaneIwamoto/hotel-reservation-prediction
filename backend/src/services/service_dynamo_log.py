import boto3
import os
from botocore.exceptions import ClientError
from uuid import uuid4
from datetime import datetime

def create_dynamodb_table(table_name):
    dynamodb = boto3.resource('dynamodb')

    try:
        client = boto3.client('dynamodb')
        tables = client.list_tables()

        if table_name not in tables['TableNames']:
            table = dynamodb.create_table(
                TableName=table_name,
                KeySchema=[
                    {
                        'AttributeName': 'id',
                        'KeyType': 'HASH'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'id',
                        'AttributeType': 'S'
                    }
                ],
                BillingMode='PAY_PER_REQUEST'
            )
            table.meta.client.get_waiter('table_exists').wait(TableName=table_name)
            print(f"Table '{table_name}' created successfully")
        else:
            print("Table already exists")
    except ClientError as e:
        print(f"Error creating DynamoDB table: {e}")

# Service Dynamo log inference
def log_inference_result(inference_params, result):
    table_name = os.environ.get('DYNAMODB_TABLE_NAME')
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)        

    log_entry = {
        'id': str(uuid4()),
        'timestamp': datetime.utcnow().isoformat(),
        'inference_params': inference_params,
        'result': result
    }
    
    try:
        table.put_item(Item=log_entry)
        print("Inference result logged in DynamoDB")
    except ClientError as e:
        print(f"Error logging inference result to DynamoDB: {e}")