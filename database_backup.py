import sys
from datetime import datetime
from time import sleep
import boto3

db_path = "/home/aerotract/.sandbox/companydb.db"
bucket = "companydb-backups"

def upload_db_to_s3(s3_filename):
    s3_client = boto3.client('s3')
    s3_client.upload_file(db_path, bucket, filename)

if __name__ == "__main__":
    while True:
        filename = datetime.now().strftime("%Y_%m_%d_%H_%M") + ".db_backup"
        upload_db_to_s3(filename)
        print(filename)
        print("sleeping for a day...")
        print("=================")
        sys.stdout.flush()
        sleep(24 * 60 * 60)