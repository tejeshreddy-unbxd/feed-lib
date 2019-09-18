'''
File: feed.py
Author: Tejesh Reddy (tejesh.reddy@unbxd.com)
Copyright: Unbxd, 2019

Description:
To fetch <customer_name> product catalog, convert to Unbxd feed format and upload to solution server.

Usage:
DEV  - $ python feed.py --unbxd_api_key=<dev-api-key> --unbxd_site_key=<dev-site-key>
PROD - $ python feed.py --unbxd_api_key=<prod-api-key> --unbxd_site_key=<prod-site-key>

'''

import sys
import csv
import urllib2
import json
import xmltodict
import copy
sys.path.append("../conversion")
import conversion_v2 as cv
from xml.dom import minidom
import pprint
import re

pp = pprint.PrettyPrinter(indent=4)

class <customer_name>_Unbxd_Feed_Generator(cv.Unbxd_Feed_Generator):
    def __parse__(self):

        # return products

class <customer_name>_Main(cv.UNBXD_MAIN):
    def __init__(self):
        cv.UNBXD_MAIN.__init__(self)
        self.UNBXD_UNIQUE_ID_FIELD = "uniqueId"
        
        self.GLOBAL_CONFIG = {
            'verbosity': 'debug',
            'log': '/mnt/<customer_name>/feedconverter.log',
            'mailer': 'dl-monitor@unbxd.com,support@unbxd.com',
            'api_version': cv.API_VERSION_2,
            'folder': '/mnt/<customer_name>/'
        }
        
        # self.FIELD_SCHEMA_MAPPING = {
        #    "<field_name>" :{
        #         "fieldName" : "<field_name>",
        #         "dataType" : "text",
        #         "multiValue": "true",
        #         "autoSuggest": "false"
        #     }
        # }

    def Start(self):
        self.__main__()
        <customer_name>_Unbxd_Feed_Generator(self.path).Run()
        #cv.Unbxd_Feed_Uploader(self.path, self.API, self.API_VERSION).Run()
<customer_name>_Main().Start()
 