import json
import boto3
import json
import json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Test')

    payload = {
        'userId': 'A001',
        'name': 'tanaka',
        'age': 50,
        'points': [
            129, 130, 140.7
        ]
    }

    table.put_item(Item=payload)
    response = table.get_item(Key={'userId': 'A001'})

    return {
        'statusCode': 200,
        'body': json.dumps(response['Item'], cls=DecimalEncoder)
    }
