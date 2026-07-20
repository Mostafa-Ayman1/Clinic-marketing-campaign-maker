import os 
from dotenv import load_dotenv

load_dotenv(override=True)

ALIBABA_API_KEY = os.getenv("ALIBABA_API_KEY")
ALIBABA_API_BASE = os.getenv("ALIBABA_API_BASE")
ALIBABA_MODEL = os.getenv("ALIBABA_MODEL")
