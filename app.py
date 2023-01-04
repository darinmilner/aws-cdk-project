#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws.aws_stack import AwsStack


app = cdk.App()
AwsStack(app,
    "python-ecs",
    stack_name="python-ecs",
    connection_arn="arn:aws:codestar-connections:us-east-1:157150173222:connection/135bd89b-8736-4a9a-b417-4d33d5fde26d",
)

app.synth()
