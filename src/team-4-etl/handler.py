import json
from re import split
import boto3
from urllib.parse import unquote_plus
import uuid
import requests
import csv

# def hello(event, context):
#     body = {
#         "message": "Go Serverless v2.0! Your function executed successfully!",
#         "input": event,
#     }

#     return {"statusCode": 200, "body": json.dumps(body)}
       
def start(event, context):
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    s3_client = boto3.client('s3')
    s3_object = s3_client.get_object(Bucket=bucket, Key=key)
    data = s3_object['Body'].read().decode('utf-8')
    data_as_list = data.splitlines()
    
    s = boto3.resource('s3')
    our_buck = s.Bucket(bucket)
    bucket_contents = []
    for file in our_buck.objects.all():
        bucket_contents.append(file.key)
    return bucket_contents

    # return data_as_list
    

