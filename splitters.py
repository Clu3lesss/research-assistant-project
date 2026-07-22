from langchain_text_splitters import RecursiveCharacterTextSplitter
import config
import loaders

def docs_splitter(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = config.CHUNK_SIZE,
        chunk_overlap = config.CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(docs) #not split_text()so as to preserve metadata
    return chunks


