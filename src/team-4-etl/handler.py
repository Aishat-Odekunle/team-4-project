import json
import boto3

# def hello(event, context):
#     body = {
#         "message": "Go Serverless v2.0! Your function executed successfully!",
#         "input": event,
#     }

#     return {"statusCode": 200, "body": json.dumps(body)}

def start(event, context):
    s3 = boto3.resource('s3', region_name="eu-west-1")
    print(event['Records'])


# 1. process the json
# need boto to call out to aws and get s3 file
# check if last four chars is '.csv'
# uri encoding
# figure out how to get files from s3