from aws_lambda_powertools.utilities.parser import BaseModel, Field
from utils.enums import ResponseType
import json 

class ResponseModel(BaseModel):        
    body: dict
    type: str
    
    def make_response(self):
        
        response = {
            "body": json.dumps(self.body)
        }

        match self.type:
            case ResponseType.SUCCESS.value:
                response["statusCode"] = 200
            case ResponseType.CUSTOM_ERROR.value:
                response["statusCode"] = 512                
            case ResponseType.ERROR.value:
                response["statusCode"] = 500
                
        return response