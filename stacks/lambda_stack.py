from aws_cdk import (
    aws_lambda as lb,
    aws_apigateway as apigw,
    Stack,
)
from constructs import Construct

class LambdaStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        lambda_function = lb.Function(self, 'helloworldfunction',
            runtime=lb.Runtime.PYTHON_3_8,
            code=lb.Code.from_asset('lambda'),
            handler='hello.handler'
        )

        api_gateway = apigw.LambdaRestApi(self,'helloworld',
            handler=lambda_function,
            rest_api_name='mylambdaapi'
        )



        