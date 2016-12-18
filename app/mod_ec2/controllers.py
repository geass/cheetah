# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for

import config
import boto3
from boto.ec2 import *

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_ec2 = Blueprint('ec2', __name__, url_prefix='/ec2')

@mod_ec2.route('/list/', methods=['GET', 'POST'])

def list():

	for region in config.region_list():
		
		session = boto3.Session(profile_name=config.profile)
		ec2 = session.resource('ec2')

		resourceList = []

		for vpc in ec2.vpcs.all():

			vpcDetail = {}
			vpcDetail['id'] = vpc.id

			if vpc.tags is not None:
				for tags in vpc.tags:
					if tags['Key'] == 'Name':
						vpcDetail['vpc_name'] = tags['Value']
			else:
				vpcDetail['vpc_name'] = "Default VPC"

			subnet_list = []
			for subnet in vpc.subnets.all():

				subnetDetail = {}
				subnetDetail['id'] = subnet.id

				if subnet.tags is not None:
					for tags in subnet.tags:
						if tags['Key'] == 'Name':
							subnetDetail['subnet_name'] = tags['Value']
				else:
					subnetDetail['subnet_name'] = "Default Subnet"


				instances = subnet.instances.all()

				instances_list = []
		    	###Looping all running instances
				for instance in instances:

					instancesDetail = {}

					instancesDetail['id'] = instance.id

					for tags in instance.tags:
						if tags['Key'] == 'Name':
							instancesDetail['instance_name'] = tags['Value']

					##Looping running instances security groups
					for sg in instance.security_groups:

						## get security group detail
						securityGroup = ec2.SecurityGroup(sg['GroupId'])

						instancesDetail['sg_ingress'] = securityGroup.ip_permissions
						instancesDetail['sg_egress'] = securityGroup.ip_permissions_egress

					instances_list.append(instancesDetail)

				subnetDetail['instances'] = instances_list
				subnet_list.append(subnetDetail)	

			vpcDetail['subnets'] = subnet_list


			resourceList.append(vpcDetail)

	return render_template("ec2/list.html", resources=resourceList)
