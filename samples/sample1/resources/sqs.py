from aws_cdk import aws_sqs, Stack

from cdk_resources import Resource, ResourceTagMixin, get_environment


class TestQueue(ResourceTagMixin, Resource[aws_sqs.Queue]):
    """ """

    construct_tags = [("environment", lambda: get_environment())]

    # Main Construct
    @classmethod
    def construct(cls, scope: Stack, id: str, **kwargs) -> aws_sqs.Queue:
        return aws_sqs.Queue(scope=scope, id=id, queue_name="test", **kwargs)
