# Instant Website Chatbot (RAG) 🚀

Transform any website into a premium, context-aware AI sales assistant instantly! Just add your website's URL to the `.env` file, and this project will crawl, index, and serve a dynamic, intelligent chatbot ready to answer user queries with your company's branding.

## Features
-   **Universal Website Support**: Works dynamically with *any* website! Just change the URL in `.env`.
-   **Context Awareness**: Remembers conversation history for natural multi-turn chat.
-   **Sales Persona**: Acts as a helpful, persuasive sales representative.
-   **Dynamic Greeting**: Personalized welcome message with your company name.
-   **Premium UI**: Modern, glassmorphism-inspired interface.
-   **Quiet Backend**: Minimal console output for a clean experience.

## Demo Video



https://github.com/user-attachments/assets/4ba9010b-569f-4f8a-9f27-fc8697f83950



## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Purva-D-Shah/instant-website-chatbot
    cd web-chatbot
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment**:
    Create a `.env` file in the root directory:
    ```env
    OPENAI_API_KEY=your_api_key_here
    WEBSITE_URLS=https://www.yourcompany.com
    COMPANY_NAME=YourCompany (Optional)
    ```

## 🌍 Deployment (Production)

This project is truly "plug-and-play." The frontend automatically routes its requests to whatever domain you host it on. 

### Recommended Platforms (Render / Railway / Heroku)
1. Fork or push this repository to your own GitHub account.
2. Go to your preferred hosting provider (e.g., [Render.com](https://render.com) or [Railway.app](https://railway.app)) and create a **New Web Service**.
3. Connect your GitHub repository.
4. Set the **Build Command**: `pip install -r requirements.txt`
5. Set the **Start Command**: `uvicorn api:app --host 0.0.0.0 --port $PORT` (The included `Procfile` should automatically handle this for you on supported platforms).
6. **Important:** In your hosting provider's dashboard, add your Environment Variables (`OPENAI_API_KEY` and `WEBSITE_URLS`).
7. Deploy! Your chatbot will be live on the URL provided by your host. No frontend configuration needed.

## 💻 Usage (Local Development)

Start the server using the batch script:
```bash
run_server.bat
```
Or manually:
```bash
py -3.13 api.py
```
Open your browser to: `http://localhost:8000`

## Tech Stack
-   **Backend**: Python, FastAPI, LangChain, ChromaDB
-   **Frontend**: HTML, CSS, JavaScript (Vanilla)
-   **AI**: OpenAI GPT-3.5/4






