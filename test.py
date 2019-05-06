#!/usr/bin/python
import requests
import json
import sys
accountid = sys.argv[1]
payload={'AUTHTOKEN':'B688DE03-B39D-4505-92A3-F6A7350CFDBD'}
r=requests.get('https://192.168.56.102:7272/restapi/json/v1/resources/304/accounts/'+accountid+'/password' , params=payload , verify=False)
b=json.loads(r.content)
c=b['operation']['Details']
a=c.get('PASSWORD')
a=a.rstrip()
print a
