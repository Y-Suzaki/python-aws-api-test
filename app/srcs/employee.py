import json


def get_list(event, context):
    body = {
        'id': '001',
        'name': 'tanaka',
        'address': 'Tokyo',
        'age': '30'
    }

    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }
    return response
