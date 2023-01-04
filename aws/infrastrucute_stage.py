from pathlib import Path
from aws_cdk import (
    Stack,
    Stage,
    aws_ec2 as ec2,
    aws_ecs as ecs,

)
from constructs import Construct

class InfrastructureStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(self, "vpc", max_azs=2)
        self.cluster = ecs.Cluster(self, "fargate-cluster", vpc=self.vpc)


class InfrastructureStage(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.stack = InfrastructureStack(self, "infra-stack", **kwargs)