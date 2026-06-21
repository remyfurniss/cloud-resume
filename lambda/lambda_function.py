import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-counter')

def lambda_handler(event, context):

    response = table.update_item(
        Key={
            'id': 'visitors'
        },
        UpdateExpression='ADD #count :inc',
        ExpressionAttributeNames={
            '#count': 'count'
        },
        ExpressionAttributeValues={
            ':inc': 1
        },
        ReturnValues='UPDATED_NEW'
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'visitors': int(response['Attributes']['count'])
        })
    }