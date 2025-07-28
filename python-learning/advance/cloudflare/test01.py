import boto3
import os
from botocore.client import Config

from config.settings import (
    CF_ACCOUNT_ID,
    CF_ACCESS_KEY_ID,
    CF_SECRET_ACCESS_KEY,
    CF_BUCKET_NAME,
    DATASETS_PATH
)

# 替换成你的 Cloudflare R2 相关配置
account_id = CF_ACCOUNT_ID
access_key_id = CF_ACCESS_KEY_ID
secret_access_key = CF_SECRET_ACCESS_KEY
bucket_name = CF_BUCKET_NAME
r2_endpoint = f"https://{account_id}.r2.cloudflarestorage.com"
object_key = "datasets/test_200MB.dat"  # 上传到 R2 后的路径
local_file_path = DATASETS_PATH / "test_200MB.dat"  # 本地文件路径

# 创建 boto3 客户端
s3 = boto3.client(
    "s3",
    endpoint_url=r2_endpoint,
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    config=Config(signature_version="s3v4"),
    region_name="auto"  # 固定写法
)

# 上传文件
# s3.upload_file(local_file_path, bucket_name, object_key)

print(os.getcwd())
print("✅ 上传成功")