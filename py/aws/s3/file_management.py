import boto3
import botocore

s3 = boto3.client("s3")
BUCKET = "test_bucket"


def s3_get(key):
    try:
        data = s3.get_object(Bucket=BUCKET, Key=key)
        data = data["Body"].read()
        data = BytesIO(data).getvalue()
        return base64.b64encode(data).decode("utf-8")
    except botocore.exceptions.ClientError as ex:
        return False


def s3_set(key, img):
    bytes_io = BytesIO()
    img.save(bytes_io, format="PNG")
    bytes_io.seek(0)
    s3_set(aws_key, bytes_io)
