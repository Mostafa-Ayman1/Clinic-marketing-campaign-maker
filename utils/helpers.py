from pathlib import Path

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

def load_prompt(filename: str) -> str:
    """Load a prompt from the prompts folder."""
    with open(PROMPTS_DIR / filename, "r", encoding="utf-8") as file:
        return file.read()
    
def clean_json(text: str) -> str:
    return (
        text.strip()
        .removeprefix("```json")
        .removeprefix("```")
        .removesuffix("```")
        .strip()
    )
