from aws_lambda_powertools.utilities.data_classes import event_source, APIGatewayProxyEventV2
import boto3


dynamodb = boto3.resource('dynamodb', config=my_config)
@event_source(data_class=APIGatewayProxyEventV2)
def handler(event: APIGatewayProxyEventV2, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(TABLE_NAME)

    return {}

    