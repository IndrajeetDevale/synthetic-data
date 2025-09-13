import boto3

def parse_s3_uri(s3_uri: str):
    assert s3_uri.startswith("s3://"), f"Not a valid S3 URI: {s3_uri}"
    without_scheme = s3_uri[5:]
    bucket, _, key = without_scheme.partition("/")
    return bucket, key

def read_text(s3_uri: str) -> str:
    bucket, key = parse_s3_uri(s3_uri)
    s3 = boto3.client("s3")
    obj = s3.get_object(Bucket=bucket, Key=key)
    return obj["Body"].read().decode("utf-8")

def write_text(s3_uri: str, text: str):
    bucket, key = parse_s3_uri(s3_uri)
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket, Key=key, Body=text.encode("utf-8"), ContentType="text/plain")
