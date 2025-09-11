# bedrock_client.py
import os, json, boto3, botocore

def client():
    region = os.getenv("AWS_REGION", "us-east-1")   # default to us-west-2 (often grants first)
    print(f"[Bedrock region] {region}")
    return boto3.client("bedrock-runtime", region_name=region)

def invoke_claude(prompt: str) -> str:
    br = client()
    model_id = os.getenv("BEDROCK_MODEL_ID", "anthropic.claude-3.5-haiku-20240307-v1:0")
    print(f"[Bedrock model] {model_id}")
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 300,
        "temperature": 0.2,
        "messages": [{"role": "user", "content": [{"type": "text", "text": prompt}]}],
    }

    # in bedrock_client.py, before invoke:
    print(f"[Region] {os.getenv('AWS_REGION')}, [Model] {os.getenv('BEDROCK_MODEL_ID')}")

    try:
        resp = br.invoke_model(
            modelId=model_id,
            contentType="application/json",
            accept="application/json",
            body=json.dumps(body),
        )
        out = json.loads(resp["body"].read())
        return out["content"][0]["text"]
    except botocore.exceptions.ClientError as e:
        # Most common: AccessDenied (no model access in this region) or wrong modelId
        raise SystemExit(
            f"\n[Bedrock invoke failed]\n"
            f"  Region: {os.getenv('AWS_REGION', 'us-west-2')}\n"
            f"  Model : {model_id}\n"
            f"  Hint  : Ensure this model is ENABLED in this region and IAM allows bedrock:InvokeModel.\n"
            f"  AWS error: {e}"
        )
