import asyncio
import json
from utils.logger import log
from agents.researcher import run as researcher_agent
from agents.planner import run as planner_agent
from agents.copywriter import run as copywriter_agent
from agents.synthesizer import run as synthesizer_agent

from utils.formatter import (
    format_research,
    format_planner,
    format_copywriter,
    format_validation
)



async def run(user_request: str) :
    """
    Marketing Workflow

    1. Research the topic.
    2. Pass research to Planner & Copywriter.
    3. Run them in parallel.
    4. Generate the final campaign report.
    """

    print("=" * 60)
    print("🚀 Marketing Workflow Started")
    print("=" * 60)

    # ---------------------------------------------------------
    # Step 1: Research
    # ---------------------------------------------------------

    research = await researcher_agent(user_request)

    # ---------------------------------------------------------
    # Step 2: Shared input
    # ---------------------------------------------------------

    shared_input = json.dumps(
        {
            "user_request": user_request,
            "research": research,
        },
        ensure_ascii=False,
        indent=2,
    )

    # ---------------------------------------------------------
    # Step 3: Planner + Copywriter
    # ---------------------------------------------------------

    planner, copywriter = await asyncio.gather(
        planner_agent(shared_input),
        copywriter_agent(shared_input),
    )

    # ---------------------------------------------------------
    # Step 4: Synthesizer
    # ---------------------------------------------------------

    final_report = await synthesizer_agent(
        user_request=user_request,
        research=research,
        planner=planner,
        copywriting=copywriter,
    )

    print("✅ Marketing Workflow Finished")
    print("=" * 60)

    log("""
        Report Type : {type(final_report).__name__}
        Keys        : {list(final_report.keys())}

        Research
        --------
        Summary Length : {len(final_report['research'].get('summary', ''))}
        Insights       : {len(final_report['research'].get('market_insights', []))}
        Opportunities  : {len(final_report['research'].get('marketing_opportunities', []))}
        Constraints    : {len(final_report['research'].get('constraints', []))}

        Planner
        -------
        Campaign Name : {final_report['planner'].get('campaign_name')}
        Schedule Items: {len(final_report['planner'].get('schedule', []))}

        Copywriter
        ----------
        Theme : {final_report['copywriter'].get('campaign_theme')}
        Posts : {len(final_report['copywriter'].get('posts', []))}
        """)



    return (
    format_research(final_report),
    format_planner(final_report),
    format_copywriter(final_report),
    format_validation(final_report)
    
    
)