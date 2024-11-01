import streamlit as st
from langchain_ollama.chat_models import ChatOllama

# Set up the Streamlit app
st.title("🧠 Interactive Chat Application with Ollama and Langchain!")

# Function to generate a response from the model
def generate_response(input_text):
    try:
        model = ChatOllama(model="llama3.2:1b", base_url="http://localhost:11434/")
        response = model.invoke(input_text)
        return response.content
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return None

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []

# Input form
with st.form("llm-form"):
    text = st.text_area("Enter your question or statement:")
    submit = st.form_submit_button("Submit")

# Process user input and generate response
if submit and text:
    with st.spinner("Generating response..."):
        response = generate_response(text)
        if response:
            # Save the interaction in chat history
            st.session_state['chat_history'].append({"user": text, "ollama": response})
            st.write(f"**🧠 Ollama:** {response}")

# Display chat history
st.write("## Chat History")
for chat in reversed(st.session_state['chat_history']):
    st.write(f"**🧑 User:** {chat['user']}")
    st.write(f"**🧠 Ollama:** {chat['ollama']}")
    st.write("---")
