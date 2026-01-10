from fastapi import APIRouter
import random
import time

router = APIRouter()

@router.get("/device/status")
def device_status():
    return {
        "led": True,
        "temperature": round(random.uniform(24, 28), 1),
        "humidity": round(random.uniform(60, 80), 1),
        "loop_time": "1.2s",
        "graph": [random.randint(20,30) for _ in range(10)],
        "serial_logs": [
            "System initialized",
            "LED ON",
            f"Sensor Reading: {random.randint(24,28)}°C, {random.randint(55,75)}%",
            "Loop completed"
        ]
    }
