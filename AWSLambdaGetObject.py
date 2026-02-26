import json
#break URL string into components
import urllib.parse
#AWS SDK for python
import boto3

print('Loading function')

s3 = boto3.client('s3')

# event is object that includes payload service invoke lambda function
#context is runtime information about function or execution environment
def lambda_handler(event, context):
   
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        return response['ContentType']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e

