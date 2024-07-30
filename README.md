<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LLM Chatbot with PDF Integration</title>
</head>
<body>
    <h1>LLM Chatbot with PDF Integration</h1>
    <p>This repository contains the code for a Streamlit application that allows users to interact with PDF documents using a chatbot powered by Large Language Models (LLMs) from OpenAI. The app uses various libraries such as LangChain, PyPDF2, and FAISS for text processing and embedding.</p>
    
<h2>Features</h2>
    <ul>
        <li>Upload and read PDF files.</li>
        <li>Extract text from PDF documents.</li>
        <li>Split extracted text into manageable chunks for processing.</li>
        <li>Generate embeddings for text chunks using OpenAI Embeddings.</li>
        <li>Store and load embeddings with FAISS.</li>
        <li>Accept user questions and provide relevant answers based on the content of the uploaded PDF.</li>
    </ul>
    
<h2>Tech Stack</h2>
    <ul>
        <li><a href="https://streamlit.io/">Streamlit</a> - Web app framework for Python.</li>
        <li><a href="https://platform.openai.com/docs/models">OpenAI</a> - API for accessing language models.</li>
        <li><a href="https://python.langchain.com/">LangChain</a> - Library for building applications with language models.</li>
        <li><a href="https://pypdf2.readthedocs.io/en/latest/">PyPDF2</a> - Library for reading PDF files.</li>
        <li><a href="https://github.com/facebookresearch/faiss">FAISS</a> - Library for efficient similarity search and clustering of dense vectors.</li>
    </ul>
    
    
<h3>Prerequisites</h3>
    <p>Ensure you have the following installed:</p>
    <ul>
        <li>Python 3.7+</li>
        <li>Streamlit</li>
        <li>PyPDF2</li>
        <li>FAISS</li>
        <li>OpenAI</li>
        <li>LangChain</li>
        <li>dotenv</li>
    </ul>
    
<h3>Installation</h3>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/your-username/llm-chatbot-pdf.git
cd llm-chatbot-pdf
            </code></pre>
        </li>
        <li>Install the required packages:
            <pre><code>pip install -r requirements.txt
            </code></pre>
        </li>
        <li>Set up your OpenAI API key:
            <p>Create a <code>.env</code> file in the root directory and add your OpenAI API key:</p>
            <pre><code>OPENAI_API_KEY=your_openai_api_key
            </code></pre>
        </li>
    </ol>
    
<h3>Running the App</h3>
    <p>Start the Streamlit app:</p>
    <pre><code>streamlit run app.py
    </code></pre>
    
<h3>Usage</h3>
    <ol>
        <li>Open the app in your browser.</li>
        <li>Upload a PDF file.</li>
        <li>Enter a question related to the content of the PDF.</li>
        <li>The app will provide an answer based on the PDF content.</li>
    </ol>
    
 <h2>Code Overview</h2>
    <p>The main code is in <code>app.py</code>. Below is a brief overview:</p>
    <ul>
        <li><strong>Sidebar</strong>: Contains the app title, description, and author information.</li>
        <li><strong>Main Function</strong>: Handles PDF upload, text extraction, text splitting, and embedding generation/loading.</li>
        <li><strong>Query Handling</strong>: Accepts user questions and returns relevant answers using the OpenAI model.</li>
    </ul>


