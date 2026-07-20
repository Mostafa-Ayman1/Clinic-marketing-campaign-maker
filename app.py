from ui.gradio_app import create_ui
from agents.orchestrator import run as orchestrator



demo = create_ui(orchestrator)

if __name__ == "__main__":
    demo.launch()