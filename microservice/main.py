#main.py

from dotenv import load_dotenv
import uuid
# import loaders
# import splitters
# import vectorsrtores
# import retriever
# import agents
import research_project
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import tempfile

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_headers=["*"],
    allow_methods=["*"],
)


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    doc_id = str(uuid.uuid4())

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
        print(f"Temp file exists: {os.path.exists(tmp_path)}, size: {os.path.getsize(tmp_path)}")

    try:
        research_project.final_loding(tmp_path, doc_id)
    finally:
        os.remove(tmp_path)  # original PDF still not kept, only its embeddings are

    return {"doc_id": doc_id}



@app.post("/ask")
async def ask(question: str = Form(...), doc_id: str = Form(...)):
    answer = research_project.invoke_agent(question, doc_id)
    return {"answer": answer}