import os
from dotenv import load_dotenv

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

# Load environment variables
load_dotenv()

def initialize_sales_rag():
    # 1. Configuration
    openai_api_key = os.getenv("OPENAI_API_KEY")
    urls_str = os.getenv("WEBSITE_URLS")
    
    if not openai_api_key or openai_api_key == "your_openai_api_key_here":
        print("Error: Please set your OPENAI_API_KEY in the .env file.")
        return None

    if not urls_str:
        print("Error: Please set WEBSITE_URLS in the .env file (comma-separated).")
        return None

    urls = [url.strip() for url in urls_str.split(",")]

    # 2. Load Documents
    try:
        loader = WebBaseLoader(urls)
        docs = loader.load()
    except Exception as e:
        print(f"Error loading URLs: {e}")
        return None

    # 3. Split Documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # 4. Create Vector Database
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(documents=splits, embedding=embeddings)

    # 5. Setup LLM
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3) # Slightly creative for sales
    
    # 6. Prompts
    # System prompt for the "Sales Representative" persona
    system_template = """You are an expert Sales Representative for the company described in the following documents.
    Your goal is to be helpful, professional, and persuasive.
    Always answer the user's question based on the context provided.
    If the answer is not in the context, politely say you don't have that information but offer to connect them with a human agent.
    
    After answering a query, gently encourage the user to ask for more details or provide their contact information if they seem interested.
    Keep your responses concise (under 4 sentences) unless a detailed explanation is requested.
    
    Context:
    {context}
    
    ----------------
    """
    messages = [
        SystemMessagePromptTemplate.from_template(system_template),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
    qa_prompt = ChatPromptTemplate.from_messages(messages)

    # 7. Setup Chain with History
    # We use ConversationalRetrievalChain to handle history automatically
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=True,
        combine_docs_chain_kwargs={"prompt": qa_prompt},
        verbose=False
    )
    
    return qa_chain

