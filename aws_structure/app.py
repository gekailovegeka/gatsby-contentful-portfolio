#!/usr/bin/env python3

from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_dynamodb as dynamodb
)
AWS_BUCKET_NAME = 'devops-test-for-alpacked1'
from aws_structure.aws_structure_stack import AwsStructureStack
class TestStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        #Create s3 bucket and give it public access
        my_bucket= s3.Bucket(self,id=AWS_BUCKET_NAME,bucket_name=AWS_BUCKET_NAME,
        removal_policy=core.RemovalPolicy.DESTROY,
        #auto_delete_objects=True,
        access_control=s3.BucketAccessControl.PUBLIC_READ)
        my_bucket.grant_public_access()
        
        #my_bucket.add_to_resource_policy(iam.PolicyStatement(effect=iam.Effect.ALLOW,actions=["s3:GetObject"],resources=[my_bucket.bucket_arn],principals=[iam.Anyone()]))
            
app = core.App()
TestStack(app, "TestStack")
app.synth()
