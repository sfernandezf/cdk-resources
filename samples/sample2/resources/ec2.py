from aws_cdk import aws_ec2, Stack

from cdk_resources import Resource, ResourceType, combine_configurations

from .vpc import DefaultVpc


class PostgresSqlRdsDatabaseSg(Resource[aws_ec2.SecurityGroup]):
    """ """

    # Main Construct
    @classmethod
    def construct(cls, scope: Stack, id: str, **kwargs) -> aws_ec2.SecurityGroup:
        return aws_ec2.SecurityGroup(
            scope=scope,
            id=id,
            vpc=DefaultVpc.get(),
            description="Postgre Sql Rds DatabaseSg",
            security_group_name="Postgre Sql Rds DatabaseSg",
            **kwargs,
        )

    # Others
    sg_ingress_rules_props = dict(
        default=dict(
            ingress_rules=[
                dict(
                    connection=aws_ec2.Port.tcp(5432),
                    description="PostgreSQL",
                    peer=aws_ec2.Peer.ipv4("0.0.0.0/0"),
                )
            ]
        )
    )

    @classmethod
    def post_create(cls, construct: aws_ec2.SecurityGroup) -> None:
        sg_ingress_rules_props = combine_configurations(
            cls.sg_ingress_rules_props
        )
        for rules in sg_ingress_rules_props["ingress_rules"]:
            construct.add_ingress_rule(**rules)
