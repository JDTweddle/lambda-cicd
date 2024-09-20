import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello, from CICD actions Lambda!')  # This will be returned as the response body.
    }