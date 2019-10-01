'''
File: feed.py
Copyright: Unbxd, 2019

Description:
To fetch <customerName> product catalog, convert to Unbxd feed format and upload to solution server.

Usage:
DEV  - $ python feed.py --unbxd_api_key=<dev-api-key> --unbxd_site_key=<dev-secret-key>
PROD - $ python feed.py --unbxd_api_key=<prod-api-key> --unbxd_site_key=<prod-secret-key>

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

class <customerName>UnbxdFeedGenerator(cv.Unbxd_Feed_Generator):
    def __parse__(self):
        pass

        #return products

class <customerName>Main(cv.UNBXD_MAIN):
    def __init__(self):
        cv.UNBXD_MAIN.__init__(self)
        self.UNBXD_UNIQUE_ID_FIELD = "uniqueId"
        self.FIELD_SCHEMA_MAPPING = self.getSchema()
        self.GLOBAL_CONFIG = {
            'verbosity': 'debug',
            'log': '/mnt/<customerName>/feedconverter.log',
            'mailer': 'dl-monitor@unbxd.com,support@unbxd.com',
            'api_version': cv.API_VERSION_2,
            'folder': '/mnt/<customerName>/'
        }
        
    def getSchema(self):
        schema = {}
        try:
            with open('schema.json', 'r') as fp:
                schema = json.load(fp)
        except IOError as e:
            cv.log.info('IOError: error while loading schema.json. Using empty!')
        return schema

    def start(self):
        self.__main__()
        <customerName>UnbxdFeedGenerator(self.path).Run()
        #cv.Unbxd_Feed_Uploader(self.path, self.API, self.API_VERSION).Run()

if __name__ == '__main__':
    <customerName>Main().start()


#python feed.py --unbxd_site_key=<SITE_KEY> --unbxd_api_key=<API_KEY>
 