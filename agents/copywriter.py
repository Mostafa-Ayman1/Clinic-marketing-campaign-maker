from services.openai_client import client
from utils.helpers import load_prompt , clean_json
from services.openai_client import client
from ddgs import DDGS
import config
import json
import asyncio

SYSTEM_PROMPT = load_prompt("copywriter_prompt.txt")


async def run(user_request: str) -> dict:
    """
    Copywriter Agent
    Creates social media posts content for the campaign.
    Returns parsed JSON as dict.
    """
    print("=" * 60)
    print("✍️  Copywriter Agent Started")
    print("=" * 60)

    response = await asyncio.to_thread(
        client.responses.create,
        model=config.ALIBABA_MODEL,
        instructions=SYSTEM_PROMPT,
        input=user_request,
        temperature=0.2
    )

    raw = clean_json(response.output_text)

    try:
        result = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"❌ Copywriter returned invalid JSON: {e}\nRaw: {raw[:300]}")
        raise

    print("✅ Copywriter Agent Finished\n")
    return result