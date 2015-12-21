#!/usr/bin/env python
# coding=utf8

import os
import json

t = os.popen("netstat -natp|awk -F: '/redis-server/&&/LISTEN/{print $2}'|awk '{print $1}'").readlines()
Port = map(lambda x : x.strip().strip('\n'),t)
li = []
for i in Port:
	li.append({'#REDISPORT':i})
print json.dumps({'data':li},sort_keys=True,indent=4)
	
