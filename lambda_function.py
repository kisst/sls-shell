import os
import json


def lambda_handler(event, context):
    stream = os.popen(event["cmd"])
    output = stream.read()
    data = {}
    data["output"] = output
    json.dumps(data)
    return data
