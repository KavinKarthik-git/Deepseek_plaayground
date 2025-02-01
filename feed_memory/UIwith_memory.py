import streamlit as st
from langchain_ollama.llms import OllamaLLM
from langchain_core.messages import AIMessage, HumanMessage

# Initialize model
model = OllamaLLM(model="deepseek-r1:14b")

# Store conversation history
full_ip = []

# Title of the app
st.title("Chatbot with Memory")

# Create a text input for the user's question
user_question = st.text_input("Ask something>>")

# Display conversation history
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []

# When the user submits a question
if user_question:
    # Append user question to conversation history
    full_ip.append(HumanMessage(user_question))
    
    # Get the model's response
    result = model.invoke(full_ip)
    
    # Append AI response to conversation history
    full_ip.append(AIMessage(result))
    
    # Update session state with new conversation history
    st.session_state.conversation_history.append(f"You: {user_question}")
    st.session_state.conversation_history.append(f"Bot: {result}")
    
    # Display conversation history
    for message in st.session_state.conversation_history:
        st.write(message)
