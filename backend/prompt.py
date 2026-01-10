from dataset import get_dataset_context

def build_prompt(user_prompt: str) -> str:
    context = get_dataset_context()

    return f"""
You are an IoT learning assistant.

Real circuit examples:
{context}

User request:
{user_prompt}

Explain clearly:
- required components
- basic connection logic
- short explanation
"""