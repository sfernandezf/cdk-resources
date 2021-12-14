from aws_cdk import aws_ec2

from cdk_resources import Resource


class DefaultVpc(Resource[aws_ec2.Vpc]):
    construct_class = aws_ec2.Vpc
    construct_lookup_method = "from_lookup"
    construct_lookup_props = dict(
        dev=dict(vpc_id="fake"),
        qa=dict(vpc_id="fake"),
        stg=dict(vpc_id="fake"),
        prod=dict(vpc_id="fake"),
    )


class BaseSubnet(Resource[aws_ec2.Subnet]):
    construct_class = aws_ec2.Subnet
    construct_lookup_method = "from_subnet_id"


class DefaultPrivateDbASubnet(BaseSubnet):
    construct_lookup_props = dict(
        dev=dict(subnet_id="fake"),
        qa=dict(subnet_id="subnet-0fa0b6822e23b368d"),
        stg=dict(subnet_id="subnet-a2a3cbc6"),
        prod=dict(subnet_id="subnet-9a5892c3"),
    )


class DefaultPrivateDbBSubnet(BaseSubnet):
    construct_lookup_props = dict(
        dev=dict(subnet_id="subnet-3b89a45f"),
        qa=dict(subnet_id="subnet-0cdfc5810ff01d889"),
        stg=dict(subnet_id="subnet-1fa6c869"),
        prod=dict(subnet_id="subnet-b78cf9c1"),
    )


class DefaultPrivateDbCSubnet(BaseSubnet):
    construct_lookup_props = dict(
        dev=dict(subnet_id="subnet-42a1541f"),
        qa=dict(subnet_id="subnet-052ffc786d5914d99"),
        stg=dict(subnet_id="subnet-e006c8b9"),
        prod=dict(subnet_id="subnet-8d1760e9"),
    )
