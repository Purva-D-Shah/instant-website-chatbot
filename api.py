from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import uvicorn
import sys
import os

# Force UTF-8 encoding for stdout/stderr to prevent Windows console crashes
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

from contextlib import asynccontextmanager
from chatbot import initialize_sales_rag
import uuid

# Load environment variables
load_dotenv()

qa_chain = None
sessions = {}  # In-memory session storage: {session_id: [(query, answer), ...]}

@asynccontextmanager
async def lifespan(app: FastAPI):
    global qa_chain
    # Startup: Initialize Sales RAG
    qa_chain = initialize_sales_rag()
    yield
    # Shutdown: Clean up resources if needed

app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="static")

def get_company_name():
    # 1. Try environment variable
    name = os.getenv("COMPANY_NAME")
    if name:
        return name
    
    # 2. Try to parse from WEBSITE_URLS
    urls_str = os.getenv("WEBSITE_URLS")
    if urls_str:
        first_url = urls_str.split(",")[0].strip()
        # Extract domain name (e.g., https://www.webtual.com -> Webtual)
        try:
            from urllib.parse import urlparse
            domain = urlparse(first_url).netloc
            # Remove www. and .com/.org/etc
            if domain.startswith("www."):
                domain = domain[4:]
            name = domain.split(".")[0].capitalize()
            return name
        except:
            pass
            
    return "Our Company"

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    company_name = get_company_name()
    return templates.TemplateResponse("index.html", {"request": request, "company_name": company_name})

@app.post("/chat")
async def chat(message: str = Form(...), session_id: str = Form(None)):
    global qa_chain, sessions
    
    if not qa_chain:
        return {"error": "Chatbot not initialized. Check server logs."}
    
    # Generate session ID if not provided
    if not session_id:
        session_id = str(uuid.uuid4())
    
    # Initialize history for new sessions
    if session_id not in sessions:
        sessions[session_id] = []
    
    chat_history = sessions[session_id]
    
    try:
        # Invoke chain with history
        result = qa_chain.invoke({"question": message, "chat_history": chat_history})
        answer = result['answer']
        
        # Update history
        chat_history.append((message, answer))
        # Keep history manageable (last 10 turns)
        if len(chat_history) > 10:
            chat_history = chat_history[-10:]
            
        sessions[session_id] = chat_history
        
        return {"response": answer, "session_id": session_id}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    if not os.path.exists("static"):
        os.makedirs("static")
    print("\nChatbot server is starting...")
    port = int(os.environ.get("PORT", 8000))
    print(f"Please open your browser to: http://localhost:{port}")
    # minimal logging
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="warning")
