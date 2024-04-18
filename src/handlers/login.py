from aws_lambda_powertools.utilities.data_classes import event_source, APIGatewayProxyEventV2
import boto3
from src.utils.enums import Table

@event_source(data_class=APIGatewayProxyEventV2)
def handler(event: APIGatewayProxyEventV2, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(Table.)

    return {}

    