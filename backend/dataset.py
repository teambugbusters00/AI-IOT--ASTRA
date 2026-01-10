import requests

DATASET_URL = "https://datasets-server.huggingface.co/rows"

def get_dataset_context(limit=3):
    params = {
        "dataset": "bshada/open-schematics",
        "config": "default",
        "split": "train",
        "offset": 0,
        "length": limit
    }

    res = requests.get(DATASET_URL, params=params)
    res.raise_for_status()

    rows = res.json()["rows"]
    context = []

    for item in rows:
        row = item["row"]
        components = row.get("components_used", [])
        name = row.get("name", "")
        desc = row.get("description", "")

        if components:
            context.append(
                f"Circuit: {name}\n"
                f"Components: {', '.join(components)}\n"
                f"Description: {desc}"
            )

    return "\n\n".join(context)