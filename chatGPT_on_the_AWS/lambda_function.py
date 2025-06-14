#! /usr/bin/env python3
"""
Senior Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro

Script lambda_function.py
=========================
Aqui usamos um modelo da Anthropic, o Claude 3 Haiku, já que 
permite on-demand throughput, ou seja, pagamos apenas pelo que usamos.

Tentei usar o Claude 3.7 Sonnet, mas ele não suporta on-demand throughput. 
Para usar este modelo, preciso criar um PERFIL DE INFERÊNCIA.

Link de estudo ---> https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-runtime_example_bedrock-runtime_InvokeModel_AnthropicClaude_section.html
"""
import boto3
import json

bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

modelId = "anthropic.claude-3-haiku-20240307-v1:0"

def lambda_handler(event, context):
    print("Event: ", json.dumps(event))

    requestBody = json.loads(event["body"])
    prompt = requestBody["prompt"]
    
    # Formato correto para a API Messages do Claude 3 Haiku
    body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 400,
        "temperature": 0.3,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}]
            }
        ]
    }
    
    try:
        bedrockResponse = bedrock.invoke_model(
            modelId=modelId,
            body=json.dumps(body),
            accept="application/json",
            contentType="application/json"
        )
        
        response_body = json.loads(bedrockResponse["body"].read())
        response_text = response_body["content"][0]["text"]
        
        apiResponse = {
            "statusCode": 200,
            "body": json.dumps({
                "prompt": prompt,
                "response": response_text
            })
        }
    
    except Exception as e:
        print(f"ERROR: {str(e)}")
        apiResponse = {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }
    
    return apiResponse
