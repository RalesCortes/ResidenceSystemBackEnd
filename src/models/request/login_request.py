from aws_lambda_powertools.utilities.parser import BaseModel

class LoginRequestModel(BaseModel):
        user: str
        password: str
        subdivision: str