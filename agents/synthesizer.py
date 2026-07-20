# agents/synthesizer.py
from services.openai_client import client
from utils.helpers import load_prompt , clean_json
import config
import json
import asyncio

SYSTEM_PROMPT = load_prompt("synthesizer_prompt.txt")


async def run(
    user_request: str,
    research: dict,
    planner: dict,
    copywriting: dict,
) -> dict:
    """
    Synthesizer Agent

    Combines and validates all agent outputs.
    Returns parsed JSON.
    """

    print("=" * 60)
    print("🧩 Synthesizer Agent Started")
    print("=" * 60)

    payload = {
        "user_request": user_request,
        "research": research,
        "planner": planner,
        "copywriter": copywriting,
    }

    response = await asyncio.to_thread(
        client.responses.create,
        model=config.ALIBABA_MODEL,
        instructions=SYSTEM_PROMPT,
        input=json.dumps(
            payload,
            ensure_ascii=False,
            indent=2,
        ),
    )

    raw = clean_json(response.output_text.strip()) 
  
    try:
        result = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"❌ Synthesizer returned invalid JSON: {e}")
        print(raw[:500])
        raise

    print("✅ Synthesizer Agent Finished\n")
    
    
    return result