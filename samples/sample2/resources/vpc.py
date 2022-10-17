from aws_cdk import aws_ec2, Stack

from cdk_resources import Resource


class DefaultVpc(Resource[aws_ec2.Vpc]):
    """
    """
    # Main Construct
    @classmethod
    def construct(cls, scope: Stack, id: str, **kwargs) -> aws_ec2.Vpc:
        return aws_ec2.Vpc.from_lookup(scope, id, **kwargs)

    # Custom Environment Props
    environment_props = dict(
        dev=dict(vpc_id="fake"),
        qa=dict(vpc_id="fake"),
        stg=dict(vpc_id="fake"),
        prod=dict(vpc_id="fake"),
    )


class BaseSubnet(Resource[aws_ec2.Subnet]):
    # Main Construct
    @classmethod
    def construct(cls, scope: Stack, id: str, **kwargs) -> aws_ec2.Subnet:
        return aws_ec2.Subnet.from_subnet_id(scope, id, **kwargs)


class DefaultPrivateDbASubnet(BaseSubnet):
    # Custom Environment Props
    environment_props = dict(
        dev=dict(subnet_id="fake"),
        qa=dict(subnet_id="fake"),
        stg=dict(subnet_id="fake"),
        prod=dict(subnet_id="fake"),
    )


class DefaultPrivateDbBSubnet(BaseSubnet):
    # Custom Environment Props
    environment_props = dict(
        dev=dict(subnet_id="fake"),
        qa=dict(subnet_id="fake"),
        stg=dict(subnet_id="fake"),
        prod=dict(subnet_id="fake"),
    )


class DefaultPrivateDbCSubnet(BaseSubnet):
    # Custom Environment Props
    environment_props = dict(
        dev=dict(subnet_id="fake"),
        qa=dict(subnet_id="fake"),
        stg=dict(subnet_id="fake"),
        prod=dict(subnet_id="fake"),
    )
