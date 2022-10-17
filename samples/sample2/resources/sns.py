from aws_cdk import aws_sns

from cdk_resources import Resource


class SnsTopic(Resource[aws_sns.Topic]):
    # Main Construct
    @classmethod
    def construct(cls, **kwargs) -> aws_sns.Topic:
        return aws_sns.Topic(
            topic_name="sns-topic", display_name="sns-topic", **kwargs
        )
