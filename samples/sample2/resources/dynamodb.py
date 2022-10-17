from aws_cdk import aws_dynamodb, RemovalPolicy, Stack

from cdk_resources import Resource


class DynamoTable(Resource[aws_dynamodb.Table]):
    """ """

    # Main Construct
    @classmethod
    def construct(cls, scope: Stack, id: str, **kwargs) -> aws_dynamodb.Table:
        return aws_dynamodb.Table(
            scope=scope,
            id=id,
            table_name="dynamodb-table",
            partition_key=aws_dynamodb.Attribute(
                name="partition_key", type=aws_dynamodb.AttributeType.STRING
            ),
            billing_mode=aws_dynamodb.BillingMode.PAY_PER_REQUEST,
            point_in_time_recovery=True,
            encryption=aws_dynamodb.TableEncryption.DEFAULT,
            stream=aws_dynamodb.StreamViewType.NEW_AND_OLD_IMAGES,
            sort_key=aws_dynamodb.Attribute(
                name="sort_key", type=aws_dynamodb.AttributeType.STRING
            ),
            removal_policy=RemovalPolicy.RETAIN,
            **kwargs,
        )

    # Custom constructs
    @classmethod
    def construct_prod(cls, scope: Stack, id: str, **kwargs):
        return aws_dynamodb.Table.from_table_name(
            scope=scope, id=id, table_name="dynamodb-table", **kwargs
        )

    # Custom Environment Props
