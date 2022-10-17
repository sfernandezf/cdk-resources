from aws_cdk import aws_sqs

from cdk_resources import Resource, ResourceTagMixin, get_environment


class TestQueue(ResourceTagMixin, Resource[aws_sqs.Queue]):
    """ """

    construct_tags = [("environment", lambda: get_environment())]

    # Main Construct
    @classmethod
    def construct(cls, **kwargs) -> aws_sqs.Queue:
        return aws_sqs.Queue(queue_name="test", **kwargs)
