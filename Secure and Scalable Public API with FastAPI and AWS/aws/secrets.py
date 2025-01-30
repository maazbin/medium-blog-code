import boto3
import json
from fastapi import Header
from typing import Annotated
from settings import SECRET_NAME

import boto3
from botocore.exceptions import ClientError


def get_secret(secret_name:str,region_name:str = "us-east-1"):

    

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise {}

    secret = get_secret_value_response['SecretString']

    return json.loads(secret)


def validate_api_key(api_key: Annotated[str | None, Header()] = None):
    user_id = get_secret(SECRET_NAME).get(api_key)
    if not user_id:
        return {}
    return user_id
