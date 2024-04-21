from jose import JWTError, jwt
from datetime import datetime, timedelta
from aws_lambda_powertools.utilities.data_classes import event_source, APIGatewayProxyEventV2
from aws_lambda_powertools.utilities.parser import parse,ValidationError
from src.utils.enums import  ResponseType
from src.models.request import LoginRequestModel
from src.models.response import ResponseModel
from src.datasources.dynamo_manager import DynamoManager
from src.utils.exceptions import DynamoException


SECRET_KEY = "e5747de9a49342cfb7fafd0c05eb1508"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@event_source(data_class=APIGatewayProxyEventV2)
def handler(event: APIGatewayProxyEventV2, context):
    try:
        login_request_model:LoginRequestModel = parse(model=LoginRequestModel, event=event.body)
       
        dynamo_manager = DynamoManager()
        
        user_data = dynamo_manager.get_user_by_user_password_subdivision(
                                                            user=login_request_model.user, 
                                                            password= login_request_model.password, 
                                                            sub_division= login_request_model.subdivision)
        response = {
            "user_data": user_data,
            "access_token": create_access_token(user_data)
        }

        return ResponseModel(body = response, type = ResponseType.SUCCESS).make_response()        
    except ValidationError as e:
        return ResponseModel(body = {"message":str(e)} , type = ResponseType.CUSTOM_ERROR).make_response()
    except DynamoException as e:
        return ResponseModel(body = {"message":str(e)} , type = ResponseType.CUSTOM_ERROR).make_response()
    except Exception as e:
        return ResponseModel(body = {"message":str(e)}, type = ResponseType.ERROR).make_response()

    


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt