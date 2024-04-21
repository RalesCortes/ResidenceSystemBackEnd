from aws_lambda_powertools.utilities.parser import BaseModel, Field
from src.utils.enums import ResponseType
import json 

class ResponseModel(BaseModel):        
    body: dict
    type: str
    
    def make_response(self):
        
        response = {
            "body": json.dumps(self.body)
        }

        match self.type:
            case ResponseType.SUCCESS:
                response["errorCode"] = 200
            case ResponseType.CUSTOM_ERROR:
                response["errorCode"] = 512                
            case ResponseType.ERROR:
                response["errorCode"] = 500
                
        return response