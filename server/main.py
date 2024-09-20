from fastapi import FastAPI
from fastapi.responses import FileResponse

import time
import os

DEBUG_NAME = os.environ.get("DEBUG_NAME", "DEBUG_SYSTEM")

app = FastAPI(
    title="test_system-backend",
    version="0.0.0")
favicon_path = 'favicon.ico'

@app.get("/")
async def root():
    return {"message":"Hello World!",
            "debug_name":DEBUG_NAME,
            "time":time.time()}

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)
