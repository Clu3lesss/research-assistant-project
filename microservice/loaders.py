from langchain_community.document_loaders import PyPDFLoader
import config
import re

def filter_references(docs):
    filtered = []
    references_found = False

    for doc in docs:
        if references_found:
            continue  # skip all pages after references started

        # look for a line that's JUST "References" (not a random citation mention)
        match = re.search(r"^\s*references\s*$", doc.page_content, re.IGNORECASE | re.MULTILINE)

        if match:
            # keep only the text before "References" on this page
            doc.page_content = doc.page_content[:match.start()]
            references_found = True

        filtered.append(doc)

    return filtered

#Splitting the PDFs
def pdf_loading(path):
    loader = PyPDFLoader(path)
    docs = loader.load()
    docs = filter_references(docs)
    return docs