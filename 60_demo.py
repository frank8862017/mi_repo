#!/usr/bin/env python
#v1.0
import time
import json

output = [{"endpoint": "monitor-test-centos", "tags": "", "timestamp": int(time.time()), "metric": "agent.cpu", "value": 1.8, "counterType": "GAUGE", "step": 60}]
print json.dumps(output)
