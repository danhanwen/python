#!/usr/bin/env python

import os
import json
import urllib

site = "http://116.213.205.185/nginx_status"
con = urllib.urlopen(site).read()
print con
r = ['Active','Writing','Reading','Waiting','accepts','handled','requests']
status = [ ]

for i in r:
	status.append({'#NGINXSTATUS':i})
print json.dumps({'data':status},sort_keys=True,indent=4,separators=(',',':'))
print "danhanwen"
