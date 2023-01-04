from pathlib import Path
from aws_cdk import (
    Stack,
    CfnOutput,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
)
from constructs import Construct

class AwsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "vpc", max_azs=2)
        cluster = ecs.Cluster(self, "fargate-cluster", vpc=vpc)

        src_path = Path(__file__).parents[2].joinpath("api")
        if not src_path.exists():
            print(f"Path {src_path} does not exist")

        service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "service",
            cluster=cluster,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_asset(str(src_path)),
                container_name="app-container",
                container_port=8000
            ),
            task_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT)
        )

        service.target_group.configure_health_check(path="/hello/health")

        CfnOutput(self, "hello-endpoint", value=f"http://{service.load_balancer.load_balancer_dns_name}/hello/Coder")
