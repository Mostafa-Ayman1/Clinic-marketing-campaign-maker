from html import escape


# ==========================================================
# Helpers
# ==========================================================

def badge(text: str, color: str = "#3b82f6") -> str: # خففنا درجة الأزرق شوية عشان تنطق في الدارك مود
    return f"""
    <span style="
        background:{color};
        color:white;
        padding:4px 10px;
        border-radius:999px;
        font-size:12px;
        font-weight:600;
    ">
        {escape(text)}
    </span>
    """


def card(title: str, body: str) -> str:
    return f"""
    <div style="
        background:#1f2937; /* خلفية غامقة */
        color:#f3f4f6;      /* لون نص فاتح */
        border:1px solid #374151; /* إطار متوافق مع الدارك مود */
        border-radius:16px;
        padding:20px;
        margin-bottom:18px;
        box-shadow:0 4px 6px -1px rgba(0, 0, 0, 0.3);
    ">
        <h3 style="margin-top:0; color:#ffffff;">{escape(title)}</h3>
        {body}
    </div>
    """


# ==========================================================
# Research
# ==========================================================

def format_research(report: dict) -> str:

    summary = report.get("summary", "")

    research = report.get("research", {})

    market_insights = research.get("market_insights", [])
    marketing_opportunities = research.get("marketing_opportunities", [])
    constraints = research.get("constraints", [])

    limitations = report.get("limitations", [])
    sources = report.get("sources", [])

    html = f"""
    <h2 style="color:#ffffff;">🧠 Research Summary</h2>
    <p style="color:#d1d5db; line-height:1.7;">
        {escape(summary)}
    </p>
    """

    # ======================================================
    # Market Insights
    # ======================================================

    if market_insights:

        body = ""

        for item in market_insights:

            body += f"""
            <li style="margin-bottom:14px;">
                <b style="color:white;">
                    {escape(item.get("topic",""))}
                </b><br>

                <span style="color:#d1d5db;">
                    {escape(item.get("detail",""))}
                </span>
            """

            if item.get("quote"):
                body += f"""
                <blockquote style="
                    margin-top:8px;
                    color:#9ca3af;
                    border-left:3px solid #3b82f6;
                    padding-left:10px;
                    font-style:italic;
                ">
                    "{escape(item['quote'])}"
                </blockquote>
                """

            if item.get("source_indexes"):
                indexes = ", ".join(map(str, item["source_indexes"]))

                body += f"""
                <div style="color:#60a5fa;font-size:13px;">
                    Sources: {indexes}
                </div>
                """

            body += "</li>"

        html += card(
            "📊 Market Insights",
            f"<ul>{body}</ul>"
        )

    # ======================================================
    # Marketing Opportunities
    # ======================================================

    if marketing_opportunities:

        body = ""

        for item in marketing_opportunities:

            indexes = ", ".join(
                map(str, item.get("source_indexes", []))
            )

            body += f"""
            <li style="margin-bottom:12px;">
                <b style="color:white;">
                    {escape(item.get("topic",""))}
                </b><br>

                <span style="color:#d1d5db;">
                    {escape(item.get("detail",""))}
                </span>

                <div style="color:#60a5fa;font-size:13px;">
                    Sources: {indexes}
                </div>
            </li>
            """

        html += card(
            "🚀 Marketing Opportunities",
            f"<ul>{body}</ul>"
        )

    # ======================================================
    # Constraints
    # ======================================================

    if constraints:

        body = ""

        for item in constraints:

            indexes = ", ".join(
                map(str, item.get("source_indexes", []))
            )

            body += f"""
            <li style="margin-bottom:10px;">
                <span style="color:#d1d5db;">
                    {escape(item.get("detail",""))}
                </span>

                <div style="color:#60a5fa;font-size:13px;">
                    Sources: {indexes}
                </div>
            </li>
            """

        html += card(
            "⚠️ Constraints",
            f"<ul>{body}</ul>"
        )

    # ======================================================
    # Limitations
    # ======================================================

    if limitations:

        body = ""

        for item in limitations:

            body += f"""
            <li style="margin-bottom:8px;color:#d1d5db;">
                {escape(item)}
            </li>
            """

        html += card(
            "❗ Limitations",
            f"<ul>{body}</ul>"
        )

    # ======================================================
    # Sources
    # ======================================================

    if sources:

        body = ""

        for src in sources:

            body += f"""
            <li style="margin-bottom:10px;">
                <b style="color:white;">
                    [{src.get("index")}]
                </b>

                {escape(src.get("title",""))}

                <br>

                <a
                    href="{escape(src.get("url",""))}"
                    target="_blank"
                    style="color:#60a5fa;"
                >
                    {escape(src.get("url",""))}
                </a>
            </li>
            """

        html += card(
            "📚 Sources",
            f"<ul>{body}</ul>"
        )

    return html


# ==========================================================
# Planner
# ==========================================================
def format_planner(report: dict) -> str:

    planner = report

    overview = planner.get("campaign_overview", {})
    stages = overview.get("stages", [])

    channels = planner.get("channel_strategy", [])
    calendar = planner.get("content_calendar", [])
    kpis = planner.get("kpis", [])
    assumptions = planner.get("assumptions", [])

    html = ""

    # =====================================================
    # Campaign Goal
    # =====================================================

    html += card(
        "🎯 Campaign Goal",
        f"""
        <p style="color:#d1d5db;line-height:1.7;">
            {escape(overview.get("goal",""))}
        </p>
        """
    )

    # =====================================================
    # Campaign Stages
    # =====================================================

    if stages:

        body = ""

        for stage in stages:

            body += f"""
            <div style="
                background:#1f2937;
                padding:14px;
                margin-bottom:12px;
                border-radius:10px;
            ">

                <h4 style="margin:0;color:white;">
                    {escape(stage.get("stage",""))}
                </h4>

                <p style="margin:8px 0;color:#d1d5db;">
                    {escape(stage.get("purpose",""))}
                </p>

                <span style="color:#60a5fa;">
                    ⏳ {escape(stage.get("duration",""))}
                </span>

            </div>
            """

        html += card("🚀 Campaign Stages", body)

    # =====================================================
    # Channel Strategy
    # =====================================================

    if channels:

        rows = ""

        for item in channels:

            priority = item.get("priority", "").capitalize()

            rows += f"""
            <tr>
                <td>{escape(item.get("channel",""))}</td>
                <td>{escape(item.get("rationale",""))}</td>
                <td>{priority}</td>
            </tr>
            """

        table = f"""
        <table style="width:100%;color:#d1d5db;border-collapse:collapse;">

            <thead>

                <tr style="background:#374151;color:white;">

                    <th>Channel</th>
                    <th>Why</th>
                    <th>Priority</th>

                </tr>

            </thead>

            <tbody>

                {rows}

            </tbody>

        </table>
        """

        html += card("📣 Channel Strategy", table)

    # =====================================================
    # Content Calendar
    # =====================================================

    if calendar:

        rows = ""

        for item in calendar:

            brief = item.get("content_brief", {})

            rows += f"""
            <tr>

                <td>{escape(item.get("date_or_timing",""))}</td>

                <td>{escape(item.get("stage",""))}</td>

                <td>{escape(item.get("channel",""))}</td>

                <td>{escape(brief.get("objective",""))}</td>

                <td>{escape(brief.get("format",""))}</td>

                <td>{escape(brief.get("cta_direction",""))}</td>

            </tr>
            """

        table = f"""
        <table style="width:100%;color:#d1d5db;border-collapse:collapse;">

            <thead>

                <tr style="background:#374151;color:white;">

                    <th>Date</th>
                    <th>Stage</th>
                    <th>Channel</th>
                    <th>Objective</th>
                    <th>Format</th>
                    <th>CTA</th>

                </tr>

            </thead>

            <tbody>

                {rows}

            </tbody>

        </table>
        """

        html += card("📅 Content Calendar", table)

    # =====================================================
    # KPIs
    # =====================================================

    if kpis:

        body = ""

        for item in kpis:

            body += f"""
            <div style="
                background:#1f2937;
                padding:12px;
                border-radius:10px;
                margin-bottom:10px;
            ">

                <b style="color:white;">
                    {escape(item.get("metric",""))}
                </b>

                <br>

                <span style="color:#9ca3af;">
                    Stage:
                    {escape(item.get("stage",""))}
                </span>

                <br>

                <span style="color:#22c55e;">
                    Target:
                    {escape(item.get("target",""))}
                </span>

            </div>
            """

        html += card("📈 KPIs", body)

    # =====================================================
    # Assumptions
    # =====================================================

    if assumptions:

        body = "<ul>"

        for assumption in assumptions:

            body += f"""
            <li style="margin-bottom:8px;color:#d1d5db;">
                {escape(assumption)}
            </li>
            """

        body += "</ul>"

        html += card("⚠️ Assumptions", body)

    return html


def format_copywriter(report: dict) -> str:

    html = f"""
    <h2 style="color:#ffffff;">✍️ Campaign Theme</h2>

    <p style="color:#d1d5db; margin-bottom:24px;">
        {escape(report.get("campaign_theme", ""))}
    </p>
    """

    posts = report.get("posts", [])

    if not posts:
        return html + card(
            "No Posts",
            "<p style='color:#9ca3af;'>No posts generated.</p>"
        )

    for post in posts:

        hashtags = " ".join(post.get("hashtags", []))

        body = f"""
        <div style="margin-bottom:16px;">
            {badge(post.get("platform", "Unknown"))}
        </div>

        <p><b style="color:#ffffff;">Type</b><br>
        <span style="color:#9ca3af;">{escape(post.get("post_type", ""))}</span></p>

        <p><b style="color:#ffffff;">Headline</b></p>
        <p style="color:#ffffff;font-size:18px;font-weight:600;">
            {escape(post.get("headline", ""))}
        </p>

        <p><b style="color:#ffffff;">Caption</b></p>

        <div style="
            background:#111827;
            padding:14px;
            border-radius:10px;
            border:1px solid #374151;
            white-space:pre-wrap;
            color:#d1d5db;
            line-height:1.7;
        ">
{escape(post.get("caption", ""))}
        </div>

        <p style="margin-top:16px;">
            <b style="color:#ffffff;">Hashtags</b>
        </p>

        <p style="color:#60a5fa;">
            {escape(hashtags)}
        </p>

        <p><b style="color:#ffffff;">CTA</b></p>

        <p style="color:#d1d5db;">
            {escape(post.get("cta", ""))}
        </p>
        """

        html += card(
            f"{post.get('platform', 'Unknown')} Post",
            body,
        )

    return html

