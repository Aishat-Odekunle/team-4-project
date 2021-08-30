import json
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

# 1. process the json
# need boto to call out to aws and get s3 file
# check if last four chars is '.csv'
# uri encoding
# figure out how to get files from s3


# def start(event, context):
#     s3_client = boto3.client('s3')
#     for record in event['Records']:
#         key = unquote_plus(record['s3']['object']['key'])
#         s3_client.download_file('gen-x1-team-4-data-in', key, 'dl.csv')
       
def start(event, context):
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    s3_client = boto3.client('s3')
    s3_obj = s3_client.get_object(Bucket=bucket, Key=key)
    data = s3_obj['Body'].read().decode('utf-8')
    return data
