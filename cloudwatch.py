# -*- coding: utf-8 -*-
import boto3
# Create CloudWatch client
client = boto3.client('autoscaling')
#cloudwatch = boto3.client('cloudwatch')
response = client.describe_metric_collection_types()
#print(response)
# List metrics through the pagination interface
#paginator = cloudwatch.get_paginator()
print(response)
#for response in paginator.paginate(Dimensions=[{'Name': 'LogGroupName'}],
#                                   MetricName='IncomingLogEvents',
#                                   Namespace='AWS/Logs'):
#    print(response['Metrics'])