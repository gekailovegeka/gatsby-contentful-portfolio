#!/usr/bin/env python3

from aws_cdk import core

from aws_structure.aws_structure_stack import AwsStructureStack


app = core.App()
AwsStructureStack(app, "aws-structure")

app.synth()
