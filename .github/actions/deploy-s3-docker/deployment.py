import os
import boto3
from botocore.config import Config


def run():
  bucket = os.getenv('INPUT_BUCKET')
  bucket_region = os.getenv('INPUT_BUCKET_REGION')
  dist_folder = os.getenv('INPUT_DIST_FOLDER')

  configuration = Config(region_name=bucket_region)
  s3_client = boto3.client('s3', config=configuration)

  for root, _, files in os.walk(dist_folder):
    for file in files:
      s3_client.upload_file(
        Filename=os.path.join(root, file),
        Bucket=bucket,
        Key=file
      )
  
  website_url = f'http://{bucket}.s3-website.{bucket_region}.amazonaws.com'
  print(f'::set-output name=website-url::{website_url}')

if __name__ == '__main__':
  run()