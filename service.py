# -*- coding: utf-8 -*-
import boto3, uuid
import excel_parser

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
      s3.Object('ntto-spending-data', 'entries.csv').put(Body="\n".join(entries), ContentType='application/csv')