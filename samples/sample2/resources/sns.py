from aws_cdk import aws_sns

from cdk_resources import Resource


class SnsTopic(Resource[aws_sns.Topic]):
    construct_class = aws_sns.Topic
    construct_props = dict(
        default=dict(topic_name="sns-topic", display_name="sns-topic")
    )
