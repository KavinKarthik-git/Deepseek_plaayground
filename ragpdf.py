import streamlit as st
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

# Define prompts
no_context_prompt = ChatPromptTemplate.from_template("Question: {question}")
template = """
You are an assistant that provides answers based on context. Summarize the relevant context if necessary, and then provide a clear and concise answer to the question.
Question: {question} 
Context: {context} 
Answer:
"""

pdfs_directory = 'chat-with-pdf/pdfs/'

embeddings = OllamaEmbeddings(model="deepseek-r1:14b")
vector_store = InMemoryVectorStore(embeddings)


model = OllamaLLM(model="deepseek-r1:14b")


def upload_pdf(file):
    with open(pdfs_directory + file.name, "wb") as f:
        f.write(file.getbuffer())


def load_pdf(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents


def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    return text_splitter.split_documents(documents)


def index_docs(documents):
    vector_store.add_documents(documents)


def retrieve_docs(query):
    return vector_store.similarity_search(query)

def answer_question(question, documents):
    if not documents:  
        return model.invoke({"question": question}, prompt=no_context_prompt)
    
    context = "\n\n".join([doc.page_content for doc in documents])
    prompt = ChatPromptTemplate.from_template(template)
    
    chain = prompt | model
    return chain.invoke({"question": question, "context": context})

st.sidebar.title("Options")
st.sidebar.info("Upload your PDFs and start asking questions about the documents.")

def get_first_page_preview(file_path):
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()  
    if documents:
        return documents[0].page_content[:300]  
    return ""



uploaded_files = st.file_uploader("Upload PDFs", type="pdf", accept_multiple_files=True)
if uploaded_files:
    for uploaded_file in uploaded_files:
        with st.spinner(f"Embedding {uploaded_file.name}..."):
            try:
                progress_bar = st.progress(0)
                upload_pdf(uploaded_file)
                progress_bar.progress(20)  

                documents = load_pdf(pdfs_directory + uploaded_file.name)
                progress_bar.progress(40)  
                chunked_documents = split_text(documents)
                progress_bar.progress(60)  
                
             
                index_docs(chunked_documents)
                progress_bar.progress(80)  

                st.success(f"{uploaded_file.name} processed successfully.")
                progress_bar.progress(100)  
            except Exception as e:
                st.error(f"Error processing {uploaded_file.name}: {e}")
        
        st.subheader(f"Uploaded File: {uploaded_file.name}")

        preview_text = get_first_page_preview(pdfs_directory + uploaded_file.name)
        st.text(f"Preview of Doc: {preview_text}")
        


        


# Chat interface
question = st.text_input("Ask a Question:")
if question:
    st.chat_message("user", avatar="👤").write(question)
    related_documents = retrieve_docs(question)
    answer = answer_question(question, related_documents)
    st.chat_message("assistant", avatar="🤖").write(answer)
