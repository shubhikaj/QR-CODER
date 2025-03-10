"""
Pydantic schemas for generating QR code
"""
from pydantic import BaseModel


# Schema for POST request to create a QR code
class GenerateQRCodeRequest(BaseModel):
    data: str
