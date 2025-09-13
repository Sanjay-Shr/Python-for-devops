'''
This is a script to take a backup from local to AWS S3
boto3 -> used to do AWS tasks using Python
'''

import boto3

s3 = boto3.resource("s3")

def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3,bucket_name,region):
    s3.create_bucket(Bucket = bucket_name,
                     createBucketConfiguration={
                     'LocationConstraint': region,
                     },)
    print("bucket created successfully")

def upload_backup(s3,file_name,bucket_name,key_name):
    """
    Uploads a given backup file path to a given s3 bucket
    with a new name (Key)
    """
    data = open(file_name, 'rb') # file gets read in binary
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Bucket Uploaded Successfully")

bucket_name = "Python"
region = "us-east-2"
# create_bucket(s3,bucket_name,region)    
# show_buckets(s3)
file_name = r"C:\Users\asksa\OneDrive\Desktop\Python\backups\backup_2025-09-12.tar.gz"
upload_backup(s3,file_name,bucket_name,"my-backup.tar.gz") # function call