import os
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent
# FAISS_INDEX_DIR = Path(os.getenv("FAISS_INDEX_DIR", BASE_DIR / "faiss_index"))
 
EMBEDDING_MODEL = "mistral-embed"
AGENT_MODEL = "mistral-small-latest"
 
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
RETRIEVER_K = 3