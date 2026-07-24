from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma

from langchain_mistralai import MistralAIEmbeddings

import config

def embed(chunks, doc_id):
    #Embedding into the vector store
    embeddings = MistralAIEmbeddings(model=config.EMBEDDING_MODEL)
    vectorstore = Chroma.from_documents(chunks, 
                                        embeddings,
                                          persist_directory=f"chroma_store/{doc_id}",
                                            collection_name=doc_id,)
    return vectorstore


def load(doc_id):
    embeddings = MistralAIEmbeddings(model=config.EMBEDDING_MODEL)
    vectorstore = Chroma(
        persist_directory=f"chroma_store/{doc_id}",
        embedding_function=embeddings,
        collection_name=doc_id,
    )
    return vectorstore