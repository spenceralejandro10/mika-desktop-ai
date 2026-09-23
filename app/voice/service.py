class VoiceService:
    """Contrato inicial para entrada/salida de voz."""

    def start_listening(self):
        raise NotImplementedError("La voz se implementará en la siguiente fase.")

    def speak(self, text: str):
        raise NotImplementedError("La voz se implementará en la siguiente fase.")
