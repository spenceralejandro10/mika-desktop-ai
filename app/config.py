import os
from dotenv import load_dotenv

load_dotenv()

MIKA_NAME = os.getenv("MIKA_NAME", "Mika")
MIKA_MODEL = os.getenv("MIKA_MODEL", "gpt-5.6")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
