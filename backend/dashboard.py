from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def dashboard():
    return {
        "projects": 2,
        "components_learned": 12,
        "status": "Ready to build"
    }
