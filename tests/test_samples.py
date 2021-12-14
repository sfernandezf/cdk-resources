import os
import sys
import subprocess

from aws_cdk import core
from aws_cdk.assertions import Match, Template
import pytest

from samples.sample1.stacks import DemoStack
from samples.sample2.stacks import Sample2Stack


TEST_DATA = [
    (
        "sample1",
        DemoStack,
        [
            ("AWS::SQS::Queue", 1)
        ]
    ),
    (
        "sample2",
        Sample2Stack,
        [
            ("AWS::DynamoDB::Table", 1),
            ("AWS::EC2::SecurityGroup", 1),
            ("AWS::RDS::DBParameterGroup", 1),
            ("AWS::RDS::DBSubnetGroup", 1),
            ("AWS::SecretsManager::Secret", 1),
            ("AWS::RDS::DBCluster", 1),
            ("AWS::SNS::Topic", 1)
        ]
    )
]


@pytest.mark.parametrize("name,stack_class,template_resources", TEST_DATA)
def test_sample(name, stack_class, template_resources):
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            f"samples/{name}/requirements.txt",
        ]
    )

    stack = stack_class(
        core.App(context=dict(environment="dev")),
        name,
        env=core.Environment(account="fake", region="us-east-1")
    )
    template = Template.from_stack(stack)
    for resource, count in template_resources:
        template.resource_count_is(resource, count)