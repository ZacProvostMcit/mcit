import json
import urllib.parse

def lambda_handler(event, context):

    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        file_name = urllib.parse.unquote_plus(
            record['s3']['object']['key']
        )

        print(f"Bucket name: {bucket_name}")
        print(f"file_name: {file_name}")
        print("Status: 200 Success")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
