# initial api router
from fastapi import APIRouter, Request
import logging
import boto3
from botocore.exceptions import ClientError
from src.schemas.requests.mini_app_request import MiniAppURLRequest


router = APIRouter()

@router.post(
    '/list_mini_app',
    summary='Get list mini app API',
    response_description='Information about the user account created.',
    operation_id="get_mini_app",
)
def get_mini_app(request_data: MiniAppURLRequest):

    presigned_json = generate_presigned_url(
        "love-story-loyalki", request_data)

    return presigned_json


def generate_presigned_url(bucket_name, request_data: MiniAppURLRequest, expiry=3600):

    presigned_url_dict = dict()
    
    region = "ap-southeast-1"

    if not request_data.list_mini_app:
        return {}

    for item in request_data.list_mini_app:

        url_format = f"https://{bucket_name}.s3.{region}.amazonaws.com/mini-bundles/{item}/ver_{request_data.version}/{request_data.platform}/[name][ext]"

        presigned_url_dict[item] = url_format

    return presigned_url_dict
