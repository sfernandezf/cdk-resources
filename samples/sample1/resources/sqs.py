from aws_cdk import aws_sqs

from cdk_resources import Resource, ResourceTagMixin, get_environment


class TestQueue(ResourceTagMixin, Resource[aws_sqs.Queue]):
    construct_class = aws_sqs.Queue
    construct_props = dict(default=dict(queue_name="test"))
    construct_tags = [
        ("environment", lambda: get_environment())
    ]
