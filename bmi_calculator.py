import json
import boto3
from decimal import Decimal

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BodyMetrichubdatabase1')

def lambda_handler(event, context):
    # Retrieve input data from the API Gateway event
    height = Decimal(event['height']) / 100  # Convert height to meters
    weight = Decimal(event['weight'])
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Prepare the result
    result = {
        'height': height,
        'weight': weight,
        'bmi': round(bmi, 2)
    }

    # Save the result in DynamoDB
    table.put_item(Item=result)

    # Return the result
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'BMI calculated successfully!',
            'data': result
        })
    }
