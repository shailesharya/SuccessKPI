import boto3
import pandas as pd

s3 = boto3.client('s3')
bucket_name = 's3-bucket-name'
file_name = 'path/to/your/file.csv'
try:
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    df = pd.read_csv(response['Body'])
    print(df)
except Exception as e:
    print(f"Error reading CSV file from S3: {str(e)}")