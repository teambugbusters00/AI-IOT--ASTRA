from fastapi import APIRouter, HTTPException
from model import run_model
from prompt import build_prompt
from database import users_db
from models import GenerateRequest
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/generate")
def generate(req: GenerateRequest):
    logger.info(f"Generate request for user: {req.email}, prompt: {req.prompt[:50]}...")
    user = users_db.get(req.email)
    if not user:
        logger.error(f"Generate failed - user not found: {req.email}")
        raise HTTPException(status_code=404, detail="User not found")

    full_prompt = build_prompt(req.prompt)
    logger.info(f"Built prompt for user: {req.email}")
    output = run_model(full_prompt)
    logger.info(f"Model generated output for user: {req.email}, output length: {len(output)}")

    project = {
        "title": req.prompt,
        "result": output
    }

    if "projects" not in user:
        user["projects"] = []
    user["projects"].append(project)

    logger.info(f"Project added to user {req.email}, total projects: {len(user['projects'])}")

    return {
        "components_and_logic": output
    }