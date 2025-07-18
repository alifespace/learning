import boto3, os
from botocore.client import Config

# 替换成你的 Cloudflare R2 相关配置
account_id = "ea5c2edd90ada86c86548343c19837e9"
access_key_id = "fa51b5450d89b13aa753a9d41d9434bc"
secret_access_key = "df114c2155ee0dcbbba6768a3737bea4297ebc58e7a88c23ccf64fad54468c3a"
bucket_name = "celltrix-bucket-01"
r2_endpoint = f"https://{account_id}.r2.cloudflarestorage.com"
object_key = "datasets/test_200MB.dat"  # 上传到 R2 后的路径
local_file_path = "test_200MB.dat"  # 本地文件路径

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