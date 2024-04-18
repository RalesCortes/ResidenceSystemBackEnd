from src.utils.enums import Table
import boto3
from src.utils.exceptions import DynamoException


class DynamoManager():
    def __init__(self) -> None:        
         self.dynamo_db = boto3.resource('dynamodb')

    def get_user_by_user_password_subdivision(self,user,password,sub_division):
        query_result = self.dynamo_db.Table(Table.USER).query(
            KeyConditionExpression=Key('').eq('Arturus Ardvarkian')
        )        

        if len(query_result["Items"]) > 0:
            return query_result["Items"][0]
        else:
            raise DynamoException("User doesn't exist")