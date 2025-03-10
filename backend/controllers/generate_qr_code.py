"""
FASTApi Controller for generating QR code
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from schemas.generate_qr_code import GenerateQRCodeRequest
from lib.generator import generate_qr_code

# Create a router for this controller
router = APIRouter()


# API route to create a QR code
@router.get("/generate_qr_code")
def get_generate_qr_code(data: str):
    """
    Generate a QR code for the given data and save it at the given file path.
    """
    try:
        img = generate_qr_code(data)
        # return the image as a streaming response
        return StreamingResponse(content=img, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
