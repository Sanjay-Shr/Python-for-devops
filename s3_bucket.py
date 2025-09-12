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
    s3.create_bucket(Bucket="Python",
                     createBusketConfiguration={
                         'LocationConstraint': 'us-east-2',
                     },)
    print("bucket created successfully")

def upload_backup(s3,file_name,bucket_name,key_name):
    
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Bucket Uploaded Successfully")

bucket_name = "Python"
region = "us-east-2"
# create_bucket(s3,bucket_name,region)    
# show_buckets(s3)
file_name = "C:\Users\asksa\OneDrive\Desktop\Python\backups\backup_2025-09-12.tar.gz"
upload_backup(s3,file_name,bucket_name,"my-backup.tar.gz")