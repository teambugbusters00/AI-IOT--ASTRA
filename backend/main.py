from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, Response
import os

from auth import router as auth_router
from dashboard import router as dashboard_router
from device import router as device_router
from ai import router as ai_router

app = FastAPI(title="AI-IOT-ASTRA Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # MVP ONLY
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(device_router)
app.include_router(ai_router)

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.on_event("startup")
async def startup_event():
    print("Items:")
    for route in app.routes:
        print(f"Path: {route.path} Name: {route.name}")

