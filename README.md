# RAG Chat with Deepseek

A simple Retrieval-Augmented Generation (RAG) system that lets you chat with your local PDF documents and ask complex questions. This project uses DeepSeek, LangChain, and Streamlit to provide a fully offline and privacy-focused experience.

## Key Features

* **Local & Private:** Process your PDFs and ask questions without sending any data to the cloud.
* **Powerful LLM:** Leverages the efficient and open-source DeepSeek-R1 14B model.
* **Context-Aware Answers:** Uses RAG to retrieve relevant information from your PDFs, providing accurate and contextually appropriate responses.
* **Easy to Use:** Simple Streamlit interface for uploading PDFs and asking questions.

## Prerequisites

1. **Install Ollama:** Download and install Ollama from the official website: [Link to Ollama website]

2. Pull DeepSeek Model: Open your terminal and pull the DeepSeek-R1 14B model:

  
   ollama pull deepseek-r1:14b
   
3.Install Dependencies: Install the required Python packages:

pip install -r requirements.txt

How to Run
Clone the Repository : clone this repository
cd chat-with-pdf  # Or the name of your project directory
Run the Streamlit App:
streamlit run pdf_rag.py
Open in Browser: Streamlit will provide a URL. Open this URL in your web browser to access the application.

