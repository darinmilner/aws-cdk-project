from aws_cdk import (
    Stack,
    pipelines,
)
from constructs import Construct
from aws.infrastrucute_stage import InfrastructureStage

class AwsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, connection_arn:str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source = pipelines.CodePipelineSource.connection(
            repo_string="darinmilner/aws-cdk-project",
            branch="main",
            connection_arn=connection_arn,
        )

        base_commands = [
            "npm install -g aws-cdk",
            "pip install -r requirements.txt"
        ]

        pipeline = pipelines.CodePipeline(self, "python-ecs",
        synth=pipelines.ShellStep("Synth",
            input=source,
            commands=base_commands + ["cdk synth"]
            )
        )

        infra_stage = InfrastructureStage(self, "infra-stage")
        infra_deploy =pipeline.add_stage(infra_stage)
