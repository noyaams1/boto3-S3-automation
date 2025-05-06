import boto3
import os

s3_client = boto3.client("s3", region_name="us-east-1")
bucket_name = "student-noya-backup"
folder_path = "daily_documents"

try:
    s3_client.head_bucket(Bucket=bucket_name)
except:
    s3_client.create_bucket(Bucket=bucket_name)

print("Starting upload of daily documents…")
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        s3_client.upload_file(file_path, bucket_name, filename)
        print(f"Uploaded: {filename}")
