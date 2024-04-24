from utils.enums import Table
import boto3
from utils.exceptions import DynamoException
from boto3.dynamodb.conditions import Key, Attr


class DynamoManager():
    def __init__(self) -> None:        
         self.dynamo_db = boto3.resource('dynamodb')

    def get_user_by_user_password_subdivision(self,user,password,sub_division):
        query_result = self.dynamo_db.Table(Table.USER.value).query(
            KeyConditionExpression=Key(f'userId').eq(f'{sub_division}#{user}'),
            FilterExpression=Attr('password').eq(password)
        )        

        print(query_result)
        
        if len(query_result["Items"]) > 0:
            return query_result["Items"][0]
        else:
            raise DynamoException("User doesn't exist")