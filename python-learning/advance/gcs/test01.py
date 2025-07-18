from google.cloud import storage
import os
from pathlib import Path


def upload_directory_to_gcs(
    bucket_name: str,
    source_directory: str,
    destination_blob_prefix: str,
    project_id: str = None
):
    """
    将本地整个目录（包括其所有文件和子目录）上传到指定的GCS存储桶路径下。

    Args:
        bucket_name (str): 目标存储桶的名称。
        source_directory (str): 要上传的本地目录的路径。
        destination_blob_prefix (str): GCS中的目标“文件夹”前缀。
                                       例如 'datasets/my-parquet-data'。
        project_id (str, optional): Google Cloud 项目ID。
                                    如果通过 ADC 或环境变量已配置，可不填。
    """
    try:
        storage_client = storage.Client(project=project_id)
        bucket = storage_client.bucket(bucket_name)
    except Exception as e:
        print(f"初始化GCS客户端或获取存储桶'{bucket_name}'失败: {e}")
        print("请检查项目ID、存储桶名称、认证和权限。")
        return

    # 确保源目录存在
    print(source_directory)
    if not os.path.isdir(source_directory):
        print(f"错误: 源目录 '{source_directory}' 不存在或不是一个目录。")
        return

    # 遍历本地目录
    for local_path, _, filenames in os.walk(source_directory):
        for filename in filenames:
            local_file_path = os.path.join(local_path, filename)
            relative_path = os.path.relpath(local_file_path, source_directory)
            gcs_relative_path = relative_path.replace(os.sep, '/')
            blob_name = os.path.join(destination_blob_prefix, gcs_relative_path).replace(os.sep, '/')

            blob = bucket.blob(blob_name)
            print(f"  Uploading {local_file_path} to gs://{bucket_name}/{blob_name}")
            try:
                blob.upload_from_filename(local_file_path)
            except Exception as e:
                print(f"    ERROR: Failed to upload {local_file_path}. Reason: {e}")
    
    print(f"\n目录 '{source_directory}' 上传完成。")



# --- 示例用法 ---
if __name__ == "__main__":
    # --- 请替换为你的实际信息 ---
    my_project_id = "celltrix-learning-project"        # 你的 Google Cloud 项目 ID
    my_bucket_name = "celltrix-bucket-01"      # 你的 GCS 存储桶名称

    # 1. 指定你已经存在的本地Parquet目录
    local_parquet_dir = "C:/Users/jamesliuwj/Prjcenter/learning/python-learning/advance/gcs/fake_test.parquet"

    # 2. 定义在GCS上的目标路径前缀 (即在GCS上的“文件夹”名称)
    gcs_destination_prefix = "datasets/fake_test_from_local.parquet"

    # 3. 调用上传函数
    upload_directory_to_gcs(
        bucket_name=my_bucket_name,
        source_directory=local_parquet_dir,
        destination_blob_prefix=gcs_destination_prefix,
        project_id=my_project_id
    )

