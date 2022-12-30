from aws_cdk import (
    Aws,
    aws_apigateway as apigw,
    aws_ssm as ssm,
    Stack
)
from constructs import Construct 

class APIStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        prj_name = self.node.try_get_context("project_name")
        env_name = self.node.try_get_context("env")

        account = Aws.ACCOUNT_ID
        region = Aws.REGION

        api_gateway = apigw.RestApi(self, 'restapi',
            endpoint_types=[apigw.EndpointType.REGIONAL],
            rest_api_name=prj_name+'-service'
        )
        api_gateway.root.add_method('ANY')

        ssm.StringParameter(self,'api-gw',
            parameter_name='/'+env_name+'/api-gw-url',
            string_value='https://'+api_gateway.rest_api_id+'.execute-api.'+region+'.amazonaws.com/'
        )
        ssm.StringParameter(self,'api-gw-id',
            parameter_name='/'+env_name+'api-gw-id',
            string_value=api_gateway.rest_api_id
        )