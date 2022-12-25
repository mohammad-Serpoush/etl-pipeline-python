from minio import Minio



client = Minio(
    "localhost:9000", access_key="admin", secret_key="admin@123", secure=False)


