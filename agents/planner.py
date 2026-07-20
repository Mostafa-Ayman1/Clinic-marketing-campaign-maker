# agents/planner_agent.py
from services.openai_client import client
from utils.helpers import load_prompt , clean_json
import config
import json
import asyncio




SYSTEM_PROMPT = load_prompt("planner_prompt.txt")


async def run(user_request: str) -> dict:
    """
    Planner Agent

    Generates a publishing plan and returns it as a Python dictionary.
    """

    print("=" * 60)
    print("📅 Planner Agent Started")
    print("=" * 60)

    response = await asyncio.to_thread(
        client.responses.create,
        model=config.ALIBABA_MODEL,
        instructions=SYSTEM_PROMPT,
        input=user_request,
        temperature=0.2
    )

    if not response.output_text:
        raise ValueError("Planner returned an empty response.")

    raw = clean_json(response.output_text)

    try:
        result = json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Planner returned invalid JSON.\n\n"
            f"Response:\n{raw}"
        ) from e

    print("✅ Planner Agent Finished\n")

    return result