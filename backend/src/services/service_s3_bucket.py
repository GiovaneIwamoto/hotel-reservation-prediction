import tarfile
import boto3
from botocore.exceptions import NoCredentialsError
import os

def save_model_from_s3():
    # S3 client config
    s3_client = boto3.client('s3')
    bucket_name = os.environ.get('S3_BUCKET_NAME')
    model_key = os.environ.get('MODEL_FILE_NAME')

    # Function to download model from S3
    def download_model_from_s3(bucket_name, model_key, download_path):
        try:
            s3_client.download_file(bucket_name, model_key, download_path)
            print("Model downloaded successfully")
        except NoCredentialsError:
            print("Credentials not available")
            
    download_dir = './models'
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
   
    # Download model from S3 at path
    download_path = './models/model.tar.gz'
    download_model_from_s3(bucket_name, model_key, download_path)
    
    # Extract compressed file
    compressed_model = tarfile.open('./models/model.tar.gz','r:gz')
    compressed_model.extractall(path=download_dir)