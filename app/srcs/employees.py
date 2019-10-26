import json


def get_list(event, context):
    body = {
        'results': [
            {
                'id': '001',
                'name': 'tanaka'
            },
            {
                'id': '002',
                'name': 'sato'
            }
        ]
    }
    response = {
        'statusCode': 200,
        'body': json.dumps(body)
    }
    return response
