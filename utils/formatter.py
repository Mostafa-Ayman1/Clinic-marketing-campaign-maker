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

    research = report.get("research", {})
    print("="*80)
    print("Research Format")
    print(report)
    print(research)
    print("="*80)

    summary = research.get("summary", "")

    research_data = research.get("research", {})

    market_insights = research_data.get("market_insights", [])
    marketing_opportunities = research_data.get("marketing_opportunities", [])
    constraints = research_data.get("constraints", [])

    html = f"""
    <h2 style="color:#ffffff;">🧠 Research Summary</h2>

    <p style="color:#d1d5db;">{escape(summary)}</p>
    """

    # ==========================================================
    # Market Insights
    # ==========================================================

    if market_insights:

        items = ""

        for item in market_insights:

            items += f"""
            <li style="margin-bottom:8px;">
                <b style="color:#ffffff;">{escape(item.get("topic", ""))}</b><br>
                <span style="color:#9ca3af;">{escape(item.get("detail", ""))}</span>
            </li>
            """

        html += card(
            "📊 Market Insights",
            f"<ul style='padding-left:20px;'>{items}</ul>"
        )

    # ==========================================================
    # Marketing Opportunities
    # ==========================================================

    if marketing_opportunities:

        items = ""

        for item in marketing_opportunities:

            items += f"""
            <li style="margin-bottom:8px;">
                <b style="color:#ffffff;">{escape(item.get("topic", ""))}</b><br>
                <span style="color:#9ca3af;">{escape(item.get("detail", ""))}</span>
            </li>
            """

        html += card(
            "🚀 Marketing Opportunities",
            f"<ul style='padding-left:20px;'>{items}</ul>"
        )

    # ==========================================================
    # Constraints
    # ==========================================================

    if constraints:

        items = ""

        for item in constraints:

            if isinstance(item, dict):
                text = item.get("detail", "")
            else:
                text = str(item)

            items += f"""
            <li style="margin-bottom:8px; color:#9ca3af;">{escape(text)}</li>
            """

        html += card(
            "⚠️ Constraints",
            f"<ul style='padding-left:20px;'>{items}</ul>"
        )

    return html


# ==========================================================
# Planner
# ==========================================================

def format_planner(report: dict) -> str:

    planner = report["planner"]

    rows = ""

    for item in planner["schedule"]:

        rows += f"""
        <tr style="border-bottom: 1px solid #374151;">
            <td style="padding:10px 8px;">{item["date"]}</td>
            <td style="padding:10px 8px;">{item["time"]}</td>
            <td style="padding:10px 8px;">{item["platform"]}</td>
            <td style="padding:10px 8px;">{escape(item["post_reference"])}</td>
        </tr>
        """

    table = f"""
    <table style="
        width:100%;
        border-collapse:collapse;
        text-align:left;
        color:#d1d5db;
    ">

        <thead>
            <tr style="background:#374151; color:#ffffff;"> <!-- رأس جدول غامق -->
                <th style="padding:12px 8px; border-top-left-radius:8px;">Date</th>
                <th style="padding:12px 8px;">Time</th>
                <th style="padding:12px 8px;">Platform</th>
                <th style="padding:12px 8px; border-top-right-radius:8px;">Post</th>
            </tr>
        </thead>

        <tbody>
            {rows}
        </tbody>

    </table>
    """

    body = f"""
    <p style="margin-bottom:8px;"><b style="color:#ffffff;">Campaign:</b> <span style="color:#9ca3af;">{escape(planner["campaign_name"])}</span></p>

    <p style="margin-bottom:20px;"><b style="color:#ffffff;">Duration:</b> 
    <span style="color:#9ca3af;">{planner["start_date"]} &rarr; {planner["end_date"]}</span></p>

    {table}
    """

    return card("📅 Publishing Schedule", body)


# ==========================================================
# Copywriter
# ==========================================================

def format_copywriter(report: dict) -> str:
    
    copy = report["copywriter"]

    html = f"""
    <h2 style="color:#ffffff;">✍️ Campaign Theme</h2>

    <p style="color:#d1d5db; margin-bottom:24px;">{escape(copy["campaign_theme"])}</p>
    """

    for post in copy["posts"]:

        hashtags = " ".join(post["hashtags"])

        body = f"""

        <div style="margin-bottom:16px;">{badge(post["platform"])}</div>

        <p><b style="color:#ffffff;">Type</b><br>
        <span style="color:#9ca3af;">{escape(post["post_type"])}</span></p>

        <p><b style="color:#ffffff;">Headline</b></p>

        <p style="color:#d1d5db; font-size:1.1em;">{escape(post["headline"])}</p>

        <p><b style="color:#ffffff;">Caption</b></p>

        <p style="white-space:pre-wrap; color:#9ca3af; background:#111827; padding:12px; border-radius:8px; border:1px solid #374151;">
{escape(post["caption"])}
        </p>

        <p><b style="color:#ffffff;">Hashtags</b></p>

        <p style="color:#60a5fa;">{escape(hashtags)}</p> <!-- لون أزرق فاتح للهاشتاجات -->

        <p><b style="color:#ffffff;">CTA</b></p>

        <p style="color:#d1d5db;">{escape(post["cta"])}</p>

        """

        html += card(post["platform"] + " Post", body)

    return html


# ==========================================================
# Validation
# ==========================================================

def format_validation(report: dict) -> str:

    validation = report["campaign"]["validation"]

    # ألوان معدلة للدارك مود
    color = "#22c55e" # أخضر أزهى شوي عشان الدارك مود

    if validation["status"] != "passed":
        color = "#ef4444" # أحمر أزهى

    body = f"""

    <p style="margin-bottom:16px;">{badge(validation["status"].upper(), color)}</p>

    """

    if validation["issues"]:

        body += "<ul style='padding-left:20px;'>"

        for issue in validation["issues"]:

            body += f"<li style='color:#fca5a5; margin-bottom:8px;'>{escape(issue)}</li>" # لون أحمر فاتح للمشاكل

        body += "</ul>"

    else:

        body += "<p style='color:#86efac;'>No issues detected. Everything looks great!</p>" # لون أخضر فاتح

    return card("Validation", body)