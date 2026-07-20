import config
from openai import OpenAI

client = OpenAI(
    api_key=config.ALIBABA_API_KEY,
    base_url=config.ALIBABA_API_BASE
)