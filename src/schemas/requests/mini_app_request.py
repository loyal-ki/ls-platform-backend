from pydantic import BaseModel

class MiniAppURLRequest(BaseModel):
    """
    A class that defines the MiniAppURLRequest.
    Args:
        name: str
        platform: str
        version: int
    """

    list_mini_app: list[str]
    platform: str
    version: str
    
