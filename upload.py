import os
from minio import Minio

BUCKET_BASE_NAME = "us-financial-data-month"

buckets = [f"{BUCKET_BASE_NAME}-{month}" for month in range(1, 6)]

client = Minio(
    "localhost:9000", access_key="admin", secret_key="admin@123", secure=False)


for bucket in buckets:
    is_exist = client.bucket_exists(bucket)
    if not is_exist:
        client.make_bucket(bucket)


for index in range(1 , 6):
    files = os.scandir(f"data/2018_0{index}")
    for file in files:
        client.fput_object(buckets[index-1], file.name, f"data/2018_0{index}/{file.name}")
        print(file.name)
