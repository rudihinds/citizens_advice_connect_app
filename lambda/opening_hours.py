import os
import boto3
from botocore.exceptions import ClientError
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['SERVICES_TABLE'])

def lambda_handler(event, context):
    service_name = event['Parameters']['ServiceName']
    current_date = datetime.now().strftime('%Y-%m-%d')  # Getting current date

    try:
        response = table.get_item(
            Key={
                'serviceName': service_name,
            }
        )
        
        # check if service is in the table
        if 'Item' not in response:
            return {'error': f'Service "{service_name}" not found'}

        # check if current date is in the holiday dates
        if current_date in response['Item'].get('HolidayDates', []):
            return { 'isOpen': False }
        else:
            return { 'isOpen': True }
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'error': 'Error in fetching data from DynamoDB'}
    except Exception as e:
        print(str(e))
        return {'error': 'Unknown error occurred'}