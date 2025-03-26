import boto3
import json

def setup_bedrock_client():
    """
    Set up the AWS Bedrock client with authentication.
    You need to have AWS credentials configured in one of these ways:
    1. AWS CLI configuration (~/.aws/credentials)
    2. Environment variables (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    3. IAM role (if running on AWS)
    """
    bedrock = boto3.client(
        service_name='bedrock-runtime',
        region_name='us-east-1'  # Replace with your desired region
    )
    return bedrock

def generate_text_with_claude(prompt):
    """
    Generate text using Claude model via AWS Bedrock
    """
    bedrock = setup_bedrock_client()
    
    # Prepare the request body
    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "top_p": 0.9,
        "top_k": 250
    }
    
    # Convert the request body to JSON string
    request_body_json = json.dumps(request_body)
    
    try:
        # Call the Bedrock API
        response = bedrock.invoke_model(
            modelId='us.anthropic.claude-3-7-sonnet-20250219-v1:0',  # or 'anthropic.claude-3-sonnet-20240229-v1:0' for Claude 3
            body=request_body_json
        )
        
        # Parse the response
        response_body = json.loads(response['body'].read())
        return response_body['content'][0]['text']
    
    except Exception as e:
        print(f"Error calling Bedrock API: {str(e)}")
        return None

def main():
    # Example usage
    prompt = "What is the capital of France?"
    response = generate_text_with_claude(prompt)
    if response:
        print("Claude's response:", response)

if __name__ == "__main__":
    main() 
