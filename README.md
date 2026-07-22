# Research Assistant Project

This repository contains a small research-assistant microservice that uses a retrieval-augmented generation (RAG) pattern to answer questions about PDF research papers in plain, everyday language — with page-level citations.

The goal is simple: let you point the service at a set of PDF papers, build a FAISS vector index of the document chunks, and run an agent that answers user questions by retrieving relevant chunks and citing the source pages.

Why this project exists

- Makes technical papers easier to explore by returning concise answers with exact citations.
- Demonstrates a compact pipeline: PDF loading → text chunking → embeddings → FAISS vector store → retriever → agent.

Quick overview

- Code is contained inside the `microservice/` folder. Keep working there when running or testing locally.
- Top-level files left in the repository root: `README.md` and `.gitignore`.
- Large data directories such as the `pdfs/` and `faiss_index/` folders were removed from the `main` branch to keep the repository lightweight. Add or recreate them locally as needed.

Structure (most important files)

- `microservice/main.py` — entrypoint function `research_project()` that wires the pipeline and returns an agent.
- `microservice/loaders.py` — PDF loading utilities.
- `microservice/splitters.py` — text chunking logic.
- `microservice/vectorsrtores.py` — creates/loads FAISS vectorstore and manages embeddings.
- `microservice/retriever.py` — builds a retriever tool from the vectorstore.
- `microservice/agents.py` — creates the agent with a system prompting policy (human-friendly answers + citations).
- `microservice/requirements.txt` — the Python dependencies used by the project.

