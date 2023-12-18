# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 19:40:41 2023

@author: Ferdinand
"""

import json
import requests
from requests.exceptions import HTTPError

#Define input variables
# Provide IP-address of UMR2
UMR2_IP = "192.168.2.138"

#Define derived variables
UMR2_URL = "http://" + UMR2_IP + "/get.json?f=$.status.*"
page = requests.get(UMR2_URL).json()

jstr = (json.dumps((page), ensure_ascii=False, indent=4))

while True:
	try:
	    response = requests.get(UMR2_URL)
	    jsonResponse = response.json()
	except HTTPError as http_err:
	    response=""
	except Exception as err:
	    response=""
	if response != "":
	    jstr = (json.dumps((jsonResponse), ensure_ascii=False, indent=4))
	    f = open('UMR2-json.txt', 'w')
	    f.write(jstr)
	    break
