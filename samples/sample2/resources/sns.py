from aws_cdk import aws_sns, Stack

from cdk_resources import Resource


class SnsTopic(Resource[aws_sns.Topic]):
    # Main Construct
    @classmethod
    def construct(cls, scope: Stack, id: str, **kwargs) -> aws_sns.Topic:
        return aws_sns.Topic(
            scope=scope, id=id, topic_name="sns-topic", display_name="sns-topic", **kwargs
        )
