import os
from dotenv import load_dotenv

load_dotenv()

# --- LLM ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = "llama-3.3-70b-versatile"
HISTORY_TURNS = 3

# --- Agent ---
MAX_TOOL_ROUNDS = 5   # Maximum tool-calling loops before stopping
                      # Prevents runaway agent loops

# --- Data ---
DATA_PATH = "./data"
