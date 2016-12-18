#!/usr/bin/python
import os
import optparse

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

###########################################
#
# Parsing the command line arguments
#
#############################################

parser = optparse.OptionParser()

parser.add_option("--profile", dest="profile", default="default")

options, args = parser.parse_args()
option_dict = vars(options)

# Statement for enabling the development environment
DEBUG = True

profile =  option_dict['profile']

def region_list():
    region_list = ['us-east-1']
    return region_list