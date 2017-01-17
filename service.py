# -*- coding: utf-8 -*-
import boto3, json, uuid
import excel_parser

url_payload = { "freshen_url": "https://api.trade.gov/v1/ntto_spending_data/freshen.json?api_key="}
lambda_client = boto3.client('lambda')

def handler(event, context):
  s3 = boto3.resource('s3')
  bucket_name = event['Records'][0]['s3']['bucket']['name']
  bucket = s3.Bucket(bucket_name)

  for obj in bucket.objects.all():
    key = obj.key
    if key == 'spending_data.xlsx':
      download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
      bucket.download_file(key, download_path)
      entries = excel_parser.run(download_path)
      try:
        response = s3.Object('ntto-spending-data-csv', 'entries.csv').put(Body="\n".join(entries), ContentType='application/csv', ACL='public-read')
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
          lambda_client.invoke(FunctionName="endpoint_freshen", InvocationType='Event', Payload=json.dumps(url_payload))
          print("Freshening data...")
        return response
      except Exception as e:
        print("Error writing file to S3 bucket: ")
        print(e)
        raise e
      break