'''
This is a script to take a backup from local to AWS S3
boto3 -> used to do AWS tasks using Python
'''

import boto3

s3 = boto3.resource("s3")
def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3):
    s3.create_bucket(Bucket="Python",
                     createBusketConfiguration={
                         'LocationConstraint': 'us-east-2',
                     },)
    print("bucket created successfully")

create_bucket(s3)    
show_buckets(s3)