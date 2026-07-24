#research_project.py

import vectorsrtores
import retriever
import agents
import loaders
import splitters

def build_agent(doc_id):
    vectorstore = vectorsrtores.load(doc_id)   # loads existing Chroma collection, no re-embedding
    retriever_tool = retriever.retriever(vectorstore)
    agent = agents.agent_creation(retriever_tool)
    return agent

def invoke_agent(question, doc_id):
    agent = build_agent(doc_id)
    response = agent.invoke({
        "messages": [{"role": "user", "content": question}]
    })
    return response["messages"][-1].content

def final_loding(tmp_path, doc_id):
    docs = loaders.pdf_loading(tmp_path)
    chunks = splitters.docs_splitter(docs)
    vectorsrtores.embed(chunks, doc_id)