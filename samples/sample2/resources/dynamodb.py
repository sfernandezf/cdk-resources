from aws_cdk import aws_dynamodb, core
from cdk_resources import Resource


class DynamoTable(Resource[aws_dynamodb.Table]):
    construct_class = aws_dynamodb.Table
    construct_props = dict(
        default=dict(
            table_name="dynamodb-table",
            partition_key=aws_dynamodb.Attribute(
                name="partition_key", type=aws_dynamodb.AttributeType.STRING
            ),
            billing_mode=aws_dynamodb.BillingMode.PAY_PER_REQUEST,
            point_in_time_recovery=True,
            server_side_encryption=True,
            stream=aws_dynamodb.StreamViewType.NEW_AND_OLD_IMAGES,
            sort_key=aws_dynamodb.Attribute(
                name="sort_key", type=aws_dynamodb.AttributeType.STRING
            ),
            removal_policy=core.RemovalPolicy.RETAIN,
        )
    )

