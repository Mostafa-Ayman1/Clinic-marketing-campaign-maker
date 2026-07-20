import asyncio
import json
import config
from services.openai_client import client
from utils.helpers import load_prompt , clean_json
from utils.logger import log
from agents.researcher import run as researcher_agent
from agents.planner import run as planner_agent
from agents.copywriter import run as copywriter_agent

from utils.formatter import (
    format_research,
    format_planner,
    format_copywriter,
)
SYSTEM_PROMPT = load_prompt("orchestrator_prompt.txt")




async def run(user_request: str):

    print("=" * 60)
    print("🚀 Marketing Workflow Started")
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
        raise ValueError(
            f"Planner returned invalid JSON.\n\n"
            f"Response:\n{raw}"
        ) 
    
    # print("=" * 100)
    # print("Research Task")
    # print(f"{result.get("research_task")}")
     
    # print("=" * 100)
    # print("Planner Task")
    # print(f"{result.get("planner_task")}")

    # print("=" * 100)
    # print("Copywright Task")
    # print(f"{result.get("copywriter_task")}")

    # =====================================================
    # Research
    # =====================================================

    research = await researcher_agent(result.get("research_task"))

    print(research)
    

    # =====================================================
    # Planner + Copywriter (Parallel)
    # =====================================================

    planner_input = json.dumps(
        {
            "user_request": result.get("planner_task"),
            "research": research,
        },
        ensure_ascii=False,
        indent=2,
    )
    copyright_input = json.dumps(
        {
            "user_request": result.get("copywriter_task"),
            "research": research,
        },
        ensure_ascii=False,
        indent=2,
    )

    planner, copywriter = await asyncio.gather(
        planner_agent(planner_input),
        copywriter_agent(copyright_input),
    )

    print("✅ Marketing Workflow Finished")
    print("=" * 60)

    # =====================================================
    # Debug Logger
    # =====================================================

    log(f"""
            ============================================================
            MARKETING WORKFLOW DEBUG
            ============================================================

            User Request
            ------------
            {user_request}

            Research
            --------
            Type          : {type(research).__name__}
            Keys          : {list(research.keys()) if isinstance(research, dict) else "N/A"}

            Summary Length: {len(research.get("summary", "")) if isinstance(research, dict) else 0}

            Insights      : {len(research.get("research", {}).get("market_insights", []))}
            Opportunities : {len(research.get("research", {}).get("marketing_opportunities", []))}
            Constraints   : {len(research.get("research", {}).get("constraints", []))}
            Sources       : {len(research.get("sources", []))}

            Planner
            -------
            Type          : {type(planner).__name__}
            Keys          : {list(planner.keys()) if isinstance(planner, dict) else "N/A"}

            Goal          : {planner.get("campaign_overview", {}).get("goal", "")}
            Stages        : {len(planner.get("campaign_overview", {}).get("stages", []))}
            Channels      : {len(planner.get("channel_strategy", []))}
            Calendar      : {len(planner.get("content_calendar", []))}
            KPIs          : {len(planner.get("kpis", []))}
            Assumptions   : {len(planner.get("assumptions", []))}

            Copywriter
            ----------
            Type          : {type(copywriter).__name__}
            Keys          : {list(copywriter.keys()) if isinstance(copywriter, dict) else "N/A"}

            Campaign Theme: {copywriter.get("campaign_theme", "")}
            Posts         : {len(copywriter.get("posts", []))}

            ============================================================
            RAW RESEARCH
            ============================================================

            {json.dumps(research, ensure_ascii=False, indent=2)}

            ============================================================
            RAW PLANNER
            ============================================================

            {json.dumps(planner, ensure_ascii=False, indent=2)}

            ============================================================
            RAW COPYWRITER
            ============================================================

            {json.dumps(copywriter, ensure_ascii=False, indent=2)}
""")

    return (
        format_research(research),
        format_planner(planner),
        format_copywriter(copywriter),
    )