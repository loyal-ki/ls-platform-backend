# initial api router
from fastapi import APIRouter, Request
import logging
import boto3
from botocore.exceptions import ClientError
from src.schemas.requests.mini_app_request import MiniAppURLRequest


router = APIRouter()

SESSION_TOKEN = """IQoJb3JpZ2luX2VjEAQaDmFwLXNvdXRoZWFzdC0xIkgwRgIhANuWKn34KsbDVPPNBhOlLKJgYqtUxGa3ZR1bEppUwfQfAiEAjk8C34+6ttKhKO6aUunOnH0PR/OweuJtZra7flJcQf8q6wEIbRAAGgw4ODY3NzkyNjEzNzAiDPMdKHv5EEJp/DcPOyrIAboZoj5llSRWazJjHeaHWlt0IO8hyuO9v4y5ip5fib6lYQtT2f40oAB1Ni4X51lRXMmOZuN8wF2u3kaSN4L3267Wu5R9/ThcCTAWwxdi7k1AHivyubTkt8YPUv85eLnwuskrkAu5kLYRf/HQ1UIVb1e7PvWKl8Sok87iNKRrYrZObvlbZK34tlndZFTsTPrTlQXMuzwOHCnWzfvznHgBm4541KgvtfLATHgk0YEeWoGO5fPeA3DvLXTrmuqsly11M4uK4UcjqvsvMObo7qQGOpcBGGqY9r/LqJEPifQN+aW3R2U5M9OgV8HxgFVIvaoyRPtFJHbO34Z26QQvvB7Gw/S2XgdV18oU4AisOiSSCNya2I5QWmsUyLEXxWQx0HjUEHrbjdzYqI209rC/GuHCXwMdDaYfSn+XCDG0aal8n2my6FtXy647oqg5zv++GZDE/zZCLz6KXLtlpEXtZ8hnOoCTVDR1y+4tyQ=="""


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
