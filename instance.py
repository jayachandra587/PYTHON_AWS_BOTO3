# -*- coding: utf-8 -*-
import boto3


# Launching New Instances
ec2=boto3.resource('ec2')
#createinstance=ec2.create_instances(ImageId='ami-0a332e3e1176ecd57', MinCount=1, MaxCount=1,InstanceType="c5.large")
#stopinstance=ec2.instances.filter(InstanceIds=['i-0ab796f1f6175a846']).stop()
#startinstance=ec2.instances.filter(InstanceIds=['i-0ab796f1f6175a846']).start()    
#terminateinstance=ec2.instances.filter(InstanceIds=['i-0ab796f1f6175a846']).terminate()
#print(terminateinstance)
