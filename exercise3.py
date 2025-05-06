import boto3
import os

s3_client = boto3.client("s3", region_name="us-east-1")
bucket_name = "student-noya-backup"
folder_path = "daily_documents"

response = s3_client.list_objects_v2(Bucket=bucket_name)
existing_files = set()

if "Contents" in response:
    existing_files = {obj["Key"] for obj in response["Contents"]}


for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        if filename in existing_files:
            print(f"File already exists: {filename}")
        else:
            s3_client.upload_file(file_path, bucket_name, filename)
            print(f"Uploaded: {filename}")
