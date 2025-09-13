# Synthetic Data POC (AWS Bedrock)

This repository is a proof of concept that connects Amazon S3 with Amazon Bedrock.  
The script reads a text file from S3, sends it to a Bedrock model, and writes the output back to S3.  
The goal is to show a minimal AWS-native pipeline that can be extended into a full synthetic data generator.

---

## Features
- v0.1: Local file → Bedrock → Local file
- v0.2: S3 input → Bedrock → S3 output

---

## Prerequisites
- Python 3.10+
- AWS CLI v2.13+
- An AWS account with:
  - Model access enabled (for example, Anthropic Claude 3 Haiku in `us-east-1`)
  - IAM permissions:
    - Bedrock: `bedrock:InvokeModel`, `bedrock:ListFoundationModels`
    - S3: `s3:GetObject`, `s3:PutObject`, `s3:ListBucket`

---

## Installation
```bash
git clone https://github.com/IndrajeetDevale/synthetic-data-poc
cd synthetic-data-poc
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

---

## AWS Configuration
```bash
export AWS_PROFILE=<your-profile>
export AWS_REGION=us-east-1
export BEDROCK_MODEL_ID=anthropic.claude-3-haiku-20240307-v1:0

