#!/usr/bin/python

import requests
import json
import sys
accountid = sys.argv[1]
payload={'AUTHTOKEN':'DCD775C1-1E57-4C81-8149-DC493E91EED9'}
r=requests.get('https://10.2.5.108:7272/restapi/json/v1/resources/301/accounts/'+accountid+'/password' , params=payload , verify=False)
b=json.loads(r.content)
c=b['operation']['Details']
a=c.get('PASSWORD')
a=a.rstrip()
print a
