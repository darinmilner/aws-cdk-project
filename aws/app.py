#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws.aws_stack import AwsStack


app = cdk.App()
AwsStack(app, "aws-hello-api", stack_name="hello-api")

app.synth()
