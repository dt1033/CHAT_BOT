#LLM Chatbot with PDF Integration
This repository contains the code for a Streamlit application that allows users to interact with PDF documents using a chatbot powered by Large Language Models (LLMs) from OpenAI. The app uses various libraries such as LangChain, PyPDF2, and FAISS for text processing and embedding.

Features
Upload and read PDF files.
Extract text from PDF documents.
Split extracted text into manageable chunks for processing.
Generate embeddings for text chunks using OpenAI Embeddings.
Store and load embeddings with FAISS.
Accept user questions and provide relevant answers based on the content of the uploaded PDF.
Tech Stack
Streamlit - Web app framework for Python.
OpenAI - API for accessing language models.
LangChain - Library for building applications with language models.
PyPDF2 - Library for reading PDF files.
FAISS - Library for efficient similarity search and clustering of dense vectors.
Getting Started
Prerequisites
Ensure you have the following installed:

Python 3.7+
Streamlit
PyPDF2
FAISS
OpenAI
LangChain
dotenv

Usage
Open the app in your browser.
Upload a PDF file.
Enter a question related to the content of the PDF.
The app will provide an answer based on the PDF content.

***This code doesnt have .env file containing the OPENAI API KEY


