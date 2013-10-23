import boto.ec2
import sys
import argparse
from credentials import aws_access_key_id, aws_secret_access_key
from config import ec2_key_name, ec2_region, ec2_placement, ec2_security_group_ids, ec2_prefered_ami

conn = boto.ec2.connect_to_region(ec2_region, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key);
reservations = conn.get_all_reservations();

def list():
  for i in reservations:
    print (i.instances[0], i.instances[0].tags["Name"]);

def newec2(instance_type):
  result = conn.run_instances(ec2_prefered_ami, #ebs 12.04 64bit m1.small
    key_name=ec2_key_name,
    instance_type=instance_type,
    placement=ec2_placement,
    security_group_ids=[ec2_security_group_ids]);
  print(result);


def addtags(resource_id, name):
  res = conn.get_all_reservations();
  for i in res:
    # print i.__getattribute__
    if (i.id==resource_id):
      # print i;
      instanceid=i.instances[0].id;
    #  print ("instance id: %s", instanceid);
  conn.create_tags(instanceid, {'Name':name});


#Prepare Command Line Parser
parser = argparse.ArgumentParser(description='ec2 helper')
parser.add_argument('-l','--list', action='store_true')
parser.add_argument('-a','--add', help='specify instance_type', metavar = 'instance_type')
parser.add_argument('-t','--tag', help='add instance name: {resource_id} {name}', nargs=2, metavar = ('resource_id','desired_name'))
args = parser.parse_args()

#parse arguments
if args.list:
    list();
elif args.add:
    print args.add;
    newec2(args.add)
elif args.tag:
    addtags(args.tag[0], args.tag[1]);
