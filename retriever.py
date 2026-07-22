from langchain_core.tools import create_retriever_tool
import vectorsrtores

#How does the tool get access to the vectorstore?
def retriever(vectorstore):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    retriever_tool = create_retriever_tool(
        retriever,
        name="paper_search",
        description="Search the loaded research paper(s) for relevant information to answer questions."
    )
    return retriever_tool