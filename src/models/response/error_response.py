from aws_lambda_powertools.utilities.parser import BaseModel

class ErrorResponseModel(BaseModel):
        description: str
        