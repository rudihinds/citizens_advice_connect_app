from aws_cdk import (
    aws_dynamodb as ddb,
    core,
    aws_iam as iam,
    aws_lambda as _lambda,
)

class CitizensAdviceStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The Services table
        services_table = ddb.Table(
            self, 'ServicesTable',
            partition_key=ddb.Attribute(name='ServiceName', type=ddb.AttributeType.STRING),
            billing_mode=ddb.BillingMode.PAY_PER_REQUEST,
            removal_policy=core.RemovalPolicy.DESTROY
        )

        # The Holidays table
        holidays_table = ddb.Table(
            self, 'HolidaysTable',
            partition_key=ddb.Attribute(name='HolidayDate', type=ddb.AttributeType.STRING),
            billing_mode=ddb.BillingMode.PAY_PER_REQUEST,
            removal_policy=core.RemovalPolicy.DESTROY
        )

        # The Lambda role
        role = iam.Role(self, 'LambdaRole',
            assumed_by=iam.ServicePrincipal('lambda.amazonaws.com'),
            # managed_policies=[
            #     iam.ManagedPolicy.from_aws_managed_policy_name('service-role/AWSLambdaBasicExecutionRole')
            # ]
        )

        # The Lambda role permissions
        policy = iam.PolicyStatement(
            actions=[
                "dynamodb:PutItem",
                "dynamodb:GetItem",
                "dynamodb:Scan",
                "dynamodb:Query",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem",
            ],
            resources=[
                "*"
            ]   
        )

        role.add_to_policy(policy)
        
        # The Lambda function
        lambda_function = _lambda.Function(self, 'OpeningHoursFunction',
            runtime=_lambda.Runtime.PYTHON_3_8,
            code=_lambda.Code.asset('lambda'),
            handler='opening_hours.lambda_handler',
            role=role,
            environment={
                'SERVICES_TABLE': services_table.table_name,
                'HOLIDAYS_TABLE': holidays_table.table_name
            }
        )
        
