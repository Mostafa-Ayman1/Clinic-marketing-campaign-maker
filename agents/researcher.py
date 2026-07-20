from services.openai_client import client
from utils.helpers import load_prompt
from ddgs import DDGS
import config
import json
import asyncio

system_prompt = load_prompt("researcher_prompt.txt")

def search_web(query: str):
    with DDGS() as ddgs:
        return list(
            ddgs.text(
                query,
                max_results=5,
            )
        )

async def run(user_request: str) -> dict:
    """
    Research Agent

    1. Search the web.
    2. Send search results to the LLM.
    3. Return a structured research report.
    """

    print("=" * 60)
    print("🔍 Research Agent Started")
    print(f"Query: {user_request}")
    print("=" * 60)

   
    raw_results =  await asyncio.to_thread(
                    search_web,
                    user_request
                )

    print(f"\n✅ Found {len(raw_results)} search results\n")

    # Keep only the fields we need
    search_results = []

    for i, item in enumerate(raw_results, start=1):

        result = {
            "title": item.get("title", ""),
            "url": item.get("href", ""),
            "content": item.get("body", "")
        }

        search_results.append(result)

        print(f"Result {i}")
        print(f"Title : {result['title']}")
        print(f"URL   : {result['url']}")
        print(f"Body  : {result['content'][:200]}...")
        print("-" * 60)

    payload = {
        "user_request": user_request,
        "search_results": search_results
    }

    print("\n🤖 Sending search results to the LLM...\n")

    response = await asyncio.to_thread(
                client.responses.create,
                model=config.ALIBABA_MODEL,
                instructions=system_prompt,
                input=json.dumps(
                        payload,
                        ensure_ascii=False,
                        indent=2
            ),
        )

    print("✅ Research Agent Finished\n")
    try:
        return json.loads(response.output_text)
    except json.JSONDecodeError:
        return {
            "error": "Invalid JSON returned by LLM",
            "raw_output": response.output_text,
        }