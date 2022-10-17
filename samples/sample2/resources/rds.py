from aws_cdk import aws_rds, aws_ec2, Duration, RemovalPolicy, Stack

from cdk_resources import Resource, env

from .ec2 import PostgresSqlRdsDatabaseSg
from .vpc import (
    DefaultVpc,
    DefaultPrivateDbASubnet,
    DefaultPrivateDbBSubnet,
    DefaultPrivateDbCSubnet,
)


class PostgresSqlParameterGroup(Resource[aws_rds.ParameterGroup]):
    """ """

    # Main Construct
    @classmethod
    def construct(cls, scope: Stack, id: str, **kwargs) -> aws_rds.ParameterGroup:
        return aws_rds.ParameterGroup(
            scope,
            id,
            engine=aws_rds.DatabaseClusterEngine.aurora_postgres(
                version=aws_rds.AuroraPostgresEngineVersion.VER_9_6_19
            ),
            description="Postgre Sql Parameter Group Parameter Group",
            **kwargs,
        )


class PostgresSqlRdsDatabase(Resource[aws_rds.DatabaseCluster]):
    """ """

    # Main Construct
    @classmethod
    def construct(cls, scope: Stack, id: str, **kwargs) -> aws_rds.DatabaseCluster:
        return aws_rds.DatabaseCluster(
            scope=scope,
            id=id,
            backup=env(
                default=aws_rds.BackupProps(retention=Duration.days(3)),
                prod=aws_rds.BackupProps(retention=Duration.days(30))
            ),
            engine=aws_rds.DatabaseClusterEngine.aurora_postgres(
                version=aws_rds.AuroraPostgresEngineVersion.VER_13_4
            ),
            deletion_protection=True,
            instance_props=aws_rds.InstanceProps(
                instance_type=aws_ec2.InstanceType.of(
                    aws_ec2.InstanceClass.BURSTABLE3,
                    aws_ec2.InstanceSize.MEDIUM,
                ),
                security_groups=[PostgresSqlRdsDatabaseSg.get()],
                vpc=DefaultVpc.get(),
                vpc_subnets=aws_ec2.SubnetSelection(
                    subnets=[
                        DefaultPrivateDbASubnet.get(),
                        DefaultPrivateDbBSubnet.get(),
                        DefaultPrivateDbCSubnet.get(),
                    ]
                ),
                parameter_group=PostgresSqlParameterGroup.get(),
            ),
            instances=env(default=1, prod=2),
            port=5432,
            removal_policy=RemovalPolicy.RETAIN,
            storage_encrypted=True,
            **kwargs,
        )

    # Custom Environment Props
