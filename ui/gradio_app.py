import gradio as gr

# ==========================================================
# Clear
# ==========================================================

def clear_fields():

    empty = "<p style='color:gray'>Waiting...</p>"

    return (
        "",
        empty,
        empty,
        empty,
        empty,
    )

# ==========================================================
# Theme
# ==========================================================

try:
    theme = gr.Theme.from_hub("allenai/gradio-theme")
except Exception:
    theme = gr.themes.Soft()


def create_ui(orchestrator):
    # ==========================================================
    # UI
    # ==========================================================

    with gr.Blocks(
        title="AI Marketing Campaign Generator",
        theme=theme
    ) as demo:

        # ------------------------------------------------------

        with gr.Column(elem_id="header"):

            gr.Markdown(
                """
    # 🦷 AI Marketing Campaign Generator

    Generate a complete marketing campaign using multiple AI agents.

    Research → Planning → Copywriting 
    """
            )

        # ------------------------------------------------------

        with gr.Row():

            # ==================================================
            # LEFT PANEL
            # ==================================================

            with gr.Column(scale=2):

                user_input = gr.Textbox(
                    label="Campaign Request",
                    lines=8,
                    placeholder="Example:\nCreate a marketing campaign plan for a dental clinic offering professional teeth whitening in Cairo.",
                )

                with gr.Row():
                    submit_btn = gr.Button(
                        "🚀 Generate Campaign",
                        variant="primary",
                    )

                    clear_btn = gr.Button("Clear")

                gr.Examples(
                    examples=[
                        "Create a marketing campaign plan for a dental clinic offering professional teeth whitening in Cairo.",
                        "Create a campaign for a dermatology clinic promoting laser hair removal.",
                        "Create a campaign for a nutrition clinic promoting a weight loss program.",
                    ],
                    inputs=user_input,
                )

            # ==================================================
            # RIGHT PANEL
            # ==================================================

            with gr.Column(scale=3):

                with gr.Tabs():

                    # ------------------------------------------
                    # Research
                    # ------------------------------------------

                    with gr.Tab("🧠 Research"):
                        research_output = gr.HTML(
                            value="<p style='color:gray'>Waiting for research...</p>"
                        )

                    # ------------------------------------------
                    # Planner
                    # ------------------------------------------

                    with gr.Tab("📅 Planner"):
                        planner_output = gr.HTML(
                            value="<p style='color:gray'>Waiting for planner...</p>"
                        )

                    # ------------------------------------------
                    # Copywriter
                    # ------------------------------------------

                    with gr.Tab("✍️ Copywriter"):
                        copywriter_output = gr.HTML(
                            value="<p style='color:gray'>Waiting for copywriter...</p>"
                        )

                    # ------------------------------------------
                    # Validation
                    # ------------------------------------------

                    with gr.Tab("✅ Validation"):
                        validation_output = gr.HTML(
                            value="<p style='color:gray'>Waiting for validation...</p>"
                        )

        # ==========================================================
        # Event Listeners
        # ==========================================================

        submit_btn.click(
            fn=orchestrator,
            inputs=user_input,
            outputs=[
                research_output,
                planner_output,
                copywriter_output,
                validation_output,
            ],
        )

        user_input.submit(
            fn=orchestrator,
            inputs=user_input,
            outputs=[
                research_output,
                planner_output,
                copywriter_output,
                validation_output,
            ],
        )

        clear_btn.click(
            fn=clear_fields,
            outputs=[
                user_input,
                research_output,
                planner_output,
                copywriter_output,
                validation_output,
            ],
        )

        # ==========================================================
        # Force Dark Mode (JavaScript Injection)
        # ==========================================================
        demo.load(
            None, 
            None, 
            None, 
            js="""
            function() {
                document.body.classList.add('dark');
            }
            """
        )
    return demo
