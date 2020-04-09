# -*- coding: utf-8 -*-
import json, os, re
from . import excel_parser
from azure.storage.blob.blockblobservice import BlockBlobService

conn_str = os.environ["AzureWebJobsStorage"]
acct_name = re.search('AccountName=(.+?);', conn_str).group(1)
acct_key = re.search('AccountKey=(.+?);', conn_str).group(1)
container_name = os.environ['ContainerName']

def handler(blob):
  key = blob.name
  if 'spending_data.xlsx' in key:
    entries = excel_parser.run(blob)
    block_blob_service = BlockBlobService(account_name= acct_name, account_key = acct_key)

    data = ''
    for k, v in entries[0].items():
      data = data + k +','
    data = data+'\n'
    for thing in entries:
      for key, value in thing.items():
        if type(value)==list:
          data = data + value[0]+','
        else:
          data = data + value +','
      data = data + '\n'
    
    print(data)
    block_blob_service.create_blob_from_text(container_name=container_name, blob_name='translated/spending_data.csv', text = str(data))