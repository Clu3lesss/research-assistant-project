from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS

from langchain_mistralai import MistralAIEmbeddings

import config

def embed(chunks):
    #Embedding into the vector store
    embeddings = MistralAIEmbeddings(model=config.EMBEDDING_MODEL)
    # vector_store = FAISS.from_documents(chunks, embedding=embeddings)
    # vector_store.save_local("faiss_index")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # for doc in docs:
    #     if "reference" in doc.page_content.lower():
    #         idx = doc.page_content.lower().find("reference")
    #         print(repr(doc.page_content[max(0,idx-50):idx+50]))
    # results = vectorstore.similarity_search("What experimental results does this paper present about laser wake field acceleration?", k=1)

    # for r in results:
    #     print(r.metadata.get("page"), "-", r.page_content[:150])
    #     print("---")
    return vectorstore