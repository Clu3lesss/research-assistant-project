from dotenv import load_dotenv
import loaders
import splitters
import vectorsrtores
import retriever
import agents
load_dotenv()
#load the documents
#Path is default for the sake of testing

def research_project(path= r"C:\Academics\Rojgaar\langchain\selfProject1\pdfs"):
    #pass the path for the document in path but keep it unused because were using the default arguement here
    docs = loaders.pdf_loading(path)

    #converts the loaded text into chunks
    chunks = splitters.docs_splitter(docs)

    #Embed the chunks
    vectorsrtore = vectorsrtores.embed(chunks)

    retriever_tool = retriever.retriever(vectorsrtore)

    #Retriever tool already called in agents. No need to call again. proceeding to make the agent directly
    agent = agents.agent_creation(retriever_tool)

    #Agent created. Wrap this in a function and return the agent to test in the final tests module
    return agent





