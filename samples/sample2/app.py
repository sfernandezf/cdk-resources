import os
from aws_cdk import App, Environment

from cdk_resources import register_stacks

from .stacks import Sample2Stack


# App
app = App()
# Env and stack
aws_env = Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"],
    region=os.environ["CDK_DEFAULT_REGION"],
)

# ------------------------------------------------------------------------------
# Stacks
# ------------------------------------------------------------------------------
#
STACKS = [
    #
    # Sample2Stack: DynamoDB and SNS
    ("sample2-stack", Sample2Stack, dict(termination_protection=True)),
    #
]
register_stacks(app, aws_env, STACKS)


# Synth
app.synth()
