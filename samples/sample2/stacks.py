from cdk_resources import ResourceStack

from .resources.dynamodb import DynamoTable
from .resources.ec2 import PostgreSqlRdsDatabaseSg
from .resources.rds import PostgreSqlRdsDatabase, PostgreSqlParameterGroup
from .resources.sns import SnsTopic
from .resources.vpc import (
    DefaultVpc,
    DefaultPrivateDbASubnet,
    DefaultPrivateDbBSubnet,
    DefaultPrivateDbCSubnet,
)


class Sample2Stack(ResourceStack):
    # fmt off
    EXISTING_RESOURCES = [
        ("vpc", DefaultVpc),
        ("subnet_db_a", DefaultPrivateDbASubnet),
        ("subnet_db_b", DefaultPrivateDbBSubnet),
        ("subnet_db_c", DefaultPrivateDbCSubnet),
    ]
    # fmt off
    RESOURCES = [
        # DynamoDB
        ("dynamodb", DynamoTable),
        # RDS
        ("postgresql-sg", PostgreSqlRdsDatabaseSg),
        ("postgresql-parameter-group", PostgreSqlParameterGroup),
        ("postgresqlDb", PostgreSqlRdsDatabase),
        # SNS
        ("sns-topic", SnsTopic),
    ]
