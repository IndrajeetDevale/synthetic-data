## v0.1 - Input → Bedrock → Output
- Region: $AWS_REGION (granted model access)
- Model: $BEDROCK_MODEL_ID (on-demand)
- Run:
  export AWS_PROFILE=<your-profile>; export AWS_REGION=us-east-1
  export BEDROCK_MODEL_ID=anthropic.claude-3-haiku-20240307-v1:0
  python3 src/main.py input.txt
