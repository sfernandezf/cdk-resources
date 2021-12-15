from aws_cdk import aws_rds, core, aws_ec2

from cdk_resources import Resource

from .ec2 import PostgreSqlRdsDatabaseSg
from .vpc import (
    DefaultVpc,
    DefaultPrivateDbASubnet,
    DefaultPrivateDbBSubnet,
    DefaultPrivateDbCSubnet,
)


class PostgreSqlParameterGroup(Resource[aws_rds.ParameterGroup]):
    construct_class = aws_rds.ParameterGroup
    construct_props = dict(
        default=dict(
            engine=aws_rds.DatabaseClusterEngine.aurora_postgres(
                version=aws_rds.AuroraPostgresEngineVersion.VER_13_4
            ),
            description="Postgre Sql Parameter Group Parameter Group",
        )
    )


class PostgreSqlRdsDatabase(Resource[aws_rds.DatabaseCluster]):
    construct_class = aws_rds.DatabaseCluster
    construct_props = dict(
        default=dict(
            engine=aws_rds.DatabaseClusterEngine.aurora_postgres(
                version=aws_rds.AuroraPostgresEngineVersion.VER_13_4
            ),
            backup=aws_rds.BackupProps(retention=core.Duration.days(3)),
            deletion_protection=True,
            instance_props=lambda: aws_rds.InstanceProps(
                instance_type=aws_ec2.InstanceType.of(
                    aws_ec2.InstanceClass.BURSTABLE3,
                    aws_ec2.InstanceSize.MEDIUM,
                ),
                security_groups=[PostgreSqlRdsDatabaseSg.get()],
                vpc=DefaultVpc.get(),
                vpc_subnets=aws_ec2.SubnetSelection(
                    subnets=[
                        DefaultPrivateDbASubnet.get(),
                        DefaultPrivateDbBSubnet.get(),
                        DefaultPrivateDbCSubnet.get(),
                    ]
                ),
                parameter_group=PostgreSqlParameterGroup().construct,
            ),
            instances=1,
            port=5432,
            removal_policy=core.RemovalPolicy.RETAIN,
            storage_encrypted=True,
        ),
        prod=dict(
            backup=aws_rds.BackupProps(retention=core.Duration.days(30)),
            instances=2,
            vpc_subnets=lambda: aws_ec2.SubnetSelection(
                subnets=[
                    DefaultPrivateDbASubnet.get(),
                    DefaultPrivateDbCSubnet.get(),
                    DefaultPrivateDbCSubnet.get()
                ]
            ),
        ),
    )
