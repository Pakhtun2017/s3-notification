import boto3

def create_s3_bucket(bucket_name):
    try:
        # Create an S3 client
        s3_client = boto3.client('s3')

        # Create an S3 bucket
        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'us-east-1'  # Change to your desired region
            }
        )

        print(f'S3 bucket "{bucket_name}" created successfully.')
    except Exception as e:
        print(f'Error creating S3 bucket: {e}')


# You can export the create_s3_bucket function
def create_s3_bucket_wrapper(bucket_name):
    return create_s3_bucket(bucket_name)