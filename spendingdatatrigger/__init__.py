import logging
from .service import handler
import azure.functions as func


def main(myblob: func.InputStream):
    if "spendingdata/spending_data.xlsx" == myblob.name:
        logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")

    handler(myblob)
