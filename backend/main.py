from fastapi import FastAPI
from controllers.generate_qr_code import router as generate_qr_code_router

app = FastAPI()

app.include_router(generate_qr_code_router)