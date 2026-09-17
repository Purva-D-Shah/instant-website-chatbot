# Instant Website Chatbot 🚀

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)

A lightweight, high-performance conversational AI tool designed to instantly ingest website content and provide precise, context-aware answers to user queries. Built with Python and modern LLM frameworks.


## 🌟 Key Features

*   **Instant Web Scraping & Indexing:** Quickly crawl and parse target URLs to extract core text and structure.
*   **Context-Aware Retrieval:** Uses vector embeddings to retrieve relevant segments and generate accurate answers.
*   **Interactive UI:** Clean, responsive chat interface built for seamless user interaction.
*   **Plug-and-Play Architecture:** Easily configurable for different LLM providers and embedding models.


## 🛠️ Tech Stack

*   **Language:** Python 3.10+
*   **Interface:** Streamlit
*   **Orchestration / RAG:** LangChain / LlamaIndex (or custom pipeline)
*   **Vector Store:** ChromaDB / FAISS


## 📂 Project Structure

```text
instant-website-chatbot/
│
├── app.py                 # Main Streamlit application entry point
├── scraper.py             # Web crawling and content parsing logic
├── requirements.txt       # Project dependencies
├── .env.example           # Template for environment variables
└── README.md              # Project documentation

## Demo Video



https://github.com/user-attachments/assets/4ba9010b-569f-4f8a-9f27-fc8697f83950



## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Purva-D-Shah/instant-website-chatbot
    cd instant-website-chatbot
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment**:
    Create a `.env` file in the root directory:
    ```env
    OPENAI_API_KEY=your_api_key_here
    WEBSITE_URLS=https://www.yourcompany.com
    COMPANY_NAME=YourCompany (Optional)
    ```

5.  **Run the application:**:
    ```bash
    streamlit run app.py
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

💡 Usage
    Open the local Streamlit URL generated in your terminal (typically http://localhost:8501).
    Input the target website URL in the sidebar input field.
    Wait for the content indexing process to complete.
    Start asking questions directly related to the website's content!

🤝 Contributing
    Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
    Fork the Project
    Create your Feature Branch (git checkout -b feature/AmazingFeature)
    Commit your Changes (git commit -m 'Add some AmazingFeature')
    Push to the Branch (git origin push feature/AmazingFeature)
    Open a Pull Request

📝 License
    Distributed under the MIT License. See LICENSE for more information.
