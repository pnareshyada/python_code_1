
# code to list details of the instance
"""import boto3
ec2client = boto3.client('ec2')
response = ec2client.describe_instances()
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(instance["ImageId"])
        print(instance["InstanceId"])
        print(printout['InstanceId'])
        print(printout['InstanceType'])
        print(printout['State']['Name'])
        print(printname['Value'])
        print(printout["ImageId"])
        print(printout["KeyName"])
        print(printout["LaunchTime"])
        print(printout['PublicDnsName'])
        print(printout["VpcId"])
        print(printout["PrivateIpAddress"])


#code to list all buckets
import boto3
s3 = boto3.resource('s3')
s3client = boto3.client('s3')
response = s3client.list_buckets()
for bucket in response["Buckets"]:
    print(bucket['Name'])

# code to describe instances
import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
print(Myec2)"""

"""import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
    print(pythonins)"""
"""
import boto3
client = boto3.client('ec2')
Myec2=client.describe_instances()
for pythonins in Myec2['Reservations']:
    for printout in pythonins['Instances']:
        for printname in printout['Tags']:
            print(printout['InstanceId'])
            print(printout['InstanceType'])
            print(printout['State']['Name'])
            print(printname['Value'])
            print(printout["ImageId"])
            print(printout["KeyName"])
            print(printout["LaunchTime"])
            print(printout['PublicDnsName'])
            print(printout["VpcId"])
            print(printout["PrivateIpAddress"])

import boto3
ids = ['i-0ad48a1e73f8fc536']
ec2 = boto3.resource('ec2')
ec2.instances.filter(InstanceIds = ids).terminate()


# python code to print the iam users
import boto3
iam = boto3.client('iam')

for user in iam.list_users()['Users']:
 print("User: {0}\nUserID: {1}\nARN: {2}\nCreatedOn: {3}\n".format(
 user['UserName'],
 user['UserId'],
 user['Arn'],
 user['CreateDate']
 )
 )
"""

import boto3
import csv
ec2_cli=boto3.client(service_name='ec2')
#print(ec2_cli.describe_regions()['Regions']) 
# collecting all the regions of aws
collect_all_regions=[]
for each_region in ec2_cli.describe_regions()["Regions"]:
    collect_all_regions.append(each_region["RegionName"])
    #print(each_region["RegionName"])# to print only the region names
#print(collect_all_regions)
#writing into a file
fo=open("ec2_Data.csv",'w',newline='')
data_obj=csv.writer(fo)
data_obj.writerow(['sno','instance_id','ami_id','instance_type','key_name','private_ip_address','public_ip_address',"KeyName","VpcId"])
count=1
for each_region in collect_all_regions:
    ec2_re=boto3.resource(service_name='ec2',region_name=each_region)
    for each_ins_in_reg in ec2_re.instances.all():
        data_obj.writerow([cnt,each_ins_in_reg.instance_id,each_ins_in_reg.image_id,each_ins_in_reg.instance_type,each_ins_in_reg.key_name,each_ins_in_reg.public_ip_address,each_ins_in_reg.private_ip_address,each_ins_in_reg.key_name,each_ins_in_reg.vpc_id])
        #data_obj.writerow([bucket.name])
        #print([cnt,each_ins_in_reg.instance_id,each_ins_in_reg.instance_type,each_ins_in_reg.key_name,each_ins_in_reg.public_ip_address,each_ins_in_reg.private_ip_address])
        count+=1

fo.close()
