import streamlit as st
import pickle
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS  
from dotenv import load_dotenv 
import os
from langchain_community.llms import openai
from langchain.chains.question_answering import load_qa_chain
from langchain_community.callbacks.manager import get_openai_callback
with st.sidebar:
    st.title("LLM Chatbot which imports pdf")
    st.markdown('''
    ##About
    This app is an LLM powered chatbot built by:
    -[Streamlit](https://streamlit.io/)
    -[OpenAI](https://platform.openai.com/docs/models)
    -[Langchain](https://python.langchain.com/)
    ''')
    add_vertical_space(5)
    st.write('Made By Devansh Tripathi(Engineer)')

load_dotenv()
def main():
    st.write("Hello")
    st.header("Chat with PDF ")

    #Upload a PDF file
    pdf1  = st.file_uploader("Upload your pdf", type='pdf')
   # st.write(pdf)
    if pdf1 is not None:
        pdf_reader=PdfReader(pdf1)
        text =""
        for page in pdf_reader.pages:
            text+=page.extract_text()
        #st.write(text)
        # st.write(pdf_reader)

        text_splitter= RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks= text_splitter.split_text(text=text)
        #st.write(chunks)
#we use faiss
        #embeddings
       
        store_name=pdf1.name[:-4]       
        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl","wb") as f:
                VectorStore=pickle.load(f)
            st.write("Embeddings loaded from the disk")
        else:
            embeddings=OpenAIEmbeddings()
            VectorStore=FAISS.from_texts(chunks,embedding=embeddings)
            with open(f"{store_name}.pkl","wb") as f:
                pickle.dump(VectorStore,f)
        #accept user question
        query=st.text_input("Ask question about your pdf file")
        #st.write(query)
        if query:
            docs=VectorStore.similarity_search(query=query)

            llm=openai(model_name='gpt-3.5-turbo')
            chain=load_qa_chain(llm=llm,chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query)
                print(cb)
            st.write(response)


if __name__=='__main__':
    main()
