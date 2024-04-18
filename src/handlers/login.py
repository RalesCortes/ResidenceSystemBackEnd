from aws_lambda_powertools.utilities.data_classes import event_source, APIGatewayProxyEventV2
from aws_lambda_powertools.utilities.parser import parse,ValidationError
from src.utils.enums import  ResponseType
from src.models.request import LoginRequestModel
from src.models.response import ResponseModel
from src.datasources.dynamo_manager import DynamoManager
from src.utils.exceptions import DynamoException

@event_source(data_class=APIGatewayProxyEventV2)
def handler(event: APIGatewayProxyEventV2, context):
    try:
        login_request_model:LoginRequestModel = parse(model=LoginRequestModel, event=event.body)
       
        dynamo_manager = DynamoManager()
        
        user_data = dynamo_manager.get_user_by_user_password_subdivision(
                                                            user=login_request_model.user, 
                                                            password= login_request_model.password, 
                                                            sub_division= login_request_model.subdivision)
        
        return ResponseModel(body = user_data, type = ResponseType.SUCCESS).make_response()        
    except ValidationError as e:
        return ResponseModel(body = {"message":str(e)} , type = ResponseType.CUSTOM_ERROR).make_response()
    except DynamoException as e:
        return ResponseModel(body = {"message":str(e)} , type = ResponseType.CUSTOM_ERROR).make_response()
    except Exception as e:
        return ResponseModel(body = {"message":str(e)}, type = ResponseType.ERROR).make_response()

    