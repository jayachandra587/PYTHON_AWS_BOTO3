import boto3
#ec2=boto3.resource('ec2')
#ec2_filter=[{'Name':'instance-state-name','Values':['running',"stopped"]}]
#instances=ec2.instances.filter(Filters=ec2_filter)
#print("All instances")
#for instance in instances:
#    for tag in instance.tags:
#        if tag['Key'] == 'Name':           
#            print("INSTANCE_ID-->%s INSTANCE_TYPE-->%s INSTANCE_NAME-->%s ,INSTATNCE_STATE-->%s\n" %(instance.id,instance.instance_type,tag['Value'],instance.state['Name']))
#            


#for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
#    print(status)
            
print("All Load Balancers:")
elbclient = boto3.client('elbv2')
elblist = elbclient.describe_load_balancers()
elblisteners=elbclient.describe_listeners(LoadBalancerArn='arn:aws:elasticloadbalancing:eu-west-2:409700564323:loadbalancer/app/rtb-uk-bidder/d0d3862070ac4ff8')
targetlist=elbclient.describe_target_groups()
#targetinstancelist=elbclient.describe_target_health(TargetGroupArn='arn:aws:elasticloadbalancing:eu-west-2:409700564323:targetgroup/rtb-uk-bidder/62748fa5963be79a')
#for elb in elblist['LoadBalancers']:
#    print("Load Blancer--->"+ elb['LoadBalancerArn'])
#    for tlist in targetlist['TargetGroups']:
#        if elb['LoadBalancerArn'] == tlist['LoadBalancerArns'][0]:            
#                print("Target Group:"+ tlist['TargetGroupName'])
#                print("Target Group Urn"+tlist[''])
#    print("\n")

#print("Dergister target group")
#dergister=elbclient.deregister_targets(TargetGroupArn='arn:aws:elasticloadbalancing:eu-west-2:409700564323:targetgroup/rtb-uk-bidder/62748fa5963be79a',Targets=[ {'Id': 'i-095cf97f66bbd40d6'}])
#print(dergister)
#print('delete target_group')
#deltrgroup=elbclient.delete_target_group(TargetGroupArn='arn:aws:elasticloadbalancing:eu-west-2:409700564323:targetgroup/rtb-uk-bidder/62748fa5963be79a')
#print(deltrgroup)
print('delete listener')
#dellistener=


print(elblisteners)
#for tlist in elblist['LoadBalancers']:
#    print(tlist)
#    print("\n")



#print("\nAll target groups")
#for tlist in targetlist['TargetGroups']:
#    print(tlist)
#    print("\n")



    

