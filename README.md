# AWS Bedrock Claude API Demo

This is a simple Python script that demonstrates how to use AWS Bedrock's Claude API using boto3.

## Prerequisites

- Python 3.8 or higher
- AWS Account with Bedrock access
- AWS credentials configured

## Setup

1. Clone this repository:
```bash
git clone <your-repository-url>
cd <repository-directory>
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure AWS credentials:
   - Option 1: Using AWS CLI
   ```bash
   aws configure
   ```
   Enter your:
   - AWS Access Key ID
   - AWS Secret Access Key
   - Default region (e.g., us-east-1)
   - Default output format (json)

   - Option 2: Set environment variables
   ```bash
   export AWS_ACCESS_KEY_ID='your_access_key'
   export AWS_SECRET_ACCESS_KEY='your_secret_key'
   export AWS_DEFAULT_REGION='us-east-1'
   ```

   - Option 3: Create a role with Bedrock access and use that role
   ```bash
   export AWS_PROFILE='your_profile_name'
   ```

## Usage

1. Make sure your virtual environment is activated:
```bash
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# .\venv\Scripts\activate
```

2. Run the script:
```bash
python bedrock_claude_demo.py
```

The script will make a sample query to Claude asking about the capital of France. You can modify the prompt in the `main()` function of the script to ask different questions.

## Model Information

If you want to use Claude 3.7, you'll need to:
1. Create an inference profile in AWS Bedrock console
2. Configure Claude 3.7 in that profile
3. Use the inference profile ARN instead of the model ID
4. If you assume a role which has access to bedrock, you can use that role by setting the AWS_PROFILE environment variable to the role name.

## Error Handling

The script includes basic error handling for API calls. If you encounter any issues:
- Check your AWS credentials
- Verify you have Bedrock access enabled in your AWS account
- Ensure you're using the correct region
- Check the error message for specific details

## License

[Your chosen license] 
