from app.config import MIKA_NAME, MIKA_MODEL, OPENAI_API_KEY

SYSTEM_PROMPT = """You are Mika, a concise desktop AI assistant.
Help the user operate their computer safely. Never claim an action succeeded unless a tool confirmed it.
Ask for confirmation before destructive or sensitive actions."""

class MikaAgent:
    def __init__(self):
        self.client = None
        if OPENAI_API_KEY:
            from openai import OpenAI
            self.client = OpenAI(api_key=OPENAI_API_KEY)

    def reply(self, message: str) -> str:
        text = message.strip()
        if not text:
            return "Escribe una instrucción."
        if self.client is None:
            return f"{MIKA_NAME} está ejecutándose en modo local. Configura OPENAI_API_KEY para activar el modelo de IA."
        response = self.client.responses.create(
            model=MIKA_MODEL,
            instructions=SYSTEM_PROMPT,
            input=text,
        )
        return response.output_text
