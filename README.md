# Mika Desktop AI

Asistente virtual local para Windows con interfaz visual, voz y herramientas extensibles.

## MVP
- Interfaz de escritorio con PySide6.
- Chat de texto.
- Agente desacoplado de la UI.
- Proveedor OpenAI opcional mediante OPENAI_API_KEY.
- Herramientas locales seguras: hora, listar archivos y abrir aplicaciones permitidas.
- Arquitectura preparada para voz, memoria y avatar.

## Requisitos
- Windows 10/11
- Python 3.11+

## Instalación
```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
```

Añade tu clave en `.env` si quieres usar OpenAI. Sin clave, Mika arranca en modo local.

## Ejecutar
```powershell
python -m app.main
```

## Pruebas
```powershell
pytest
```
