import boto3

s3_client = boto3.client("s3", region_name="us-east-1")
bucket_name = "student-noya-bucket"
s3_client.create_bucket(Bucket=bucket_name)
s3_client.upload_file("./team_image.png", bucket_name, "team_image.png")
print("file uploaded correctly")
response = s3_client.list_objects_v2(Bucket=bucket_name)
print(response)
if "Contents" in response:
    for obj in response["Contents"]:
        print(f"Object under {bucket_name} :{obj["Key"]}")
else:
    print("no objects found")
