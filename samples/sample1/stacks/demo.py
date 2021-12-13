from cdk_resources import ResourceStack

from resources import TestQueue

__all__ = ["DemoStack"]


class DemoStack(ResourceStack):
    RESOURCES = [("test_queue", TestQueue)]
