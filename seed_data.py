import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

table = dynamodb.Table('ServicesTable')

data = [
    {
        'ServiceName': 'Service_One',
        'HolidayDates': ['2023-12-25', '2023-12-31']
    },
    {
        'ServiceName': 'LondHotline',
        'HolidayDates': ['2023-11-25', '2023-12-01']
    }
]

for item in data:
    table.put_item(Item=item)
