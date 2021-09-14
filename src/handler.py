import boto3
import src.app as run_etl
import csv


def start(event, context):
    key = event['Records'][0]['s3']['object']['key']
    bucket = event['Records'][0]['s3']['bucket']['name']
    s3_client = boto3.client('s3')
    s3_object = s3_client.get_object(Bucket=bucket, Key=key)
    data = s3_object['Body'].read().decode('utf-8')
    data_as_list = data.splitlines()
    
    print(len(data_as_list), 'data as list len')
    with open('/tmp/temp.csv', 'wb') as f:
        s3_client.download_fileobj(bucket, key, f)

        run_etl.etl('/tmp/temp.csv')
        return 'etl finished'
    


