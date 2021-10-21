#!/usr/bin/env python3

from aws_cdk import core

from cdk_container_stack.cdk_container_stack import ContainerStack

app = core.App()

ContainerStack(app, "cdk-container-stack")

app.synth()
