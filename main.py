import streamlit as st
import google.generativeai as ai
import shelve
import os

# Configure the API key
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
ai.configure(api_key=API_KEY)

# Initialize the chat model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

st.title("RKM Turbo")
st.subheader('How can I help you with?')

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"


# Ensure chatbot model is initialized in session state
if "chatbot_model" not in st.session_state:
    st.session_state["chatbot_model"] = "gemini-pro"

def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])

# Save chat history to shelve file
def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages

# Initialize or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()
with st.sidebar:
    if st.button("Delete history"):
        st.session_state.messages = []
        save_chat_history([])
    st.link_button("Github","https://github.com/rkm0078")
        
# Display chat history
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Main chat interface
if prompt := st.chat_input("Start Conversation"):
    # Append user message to session history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    # Send the user's message to the chatbot and get the response
    if prompt == "Who are you" and "what's your name" and "what's your name?" and "What's your name?" and "What's your name?" and "who are you" and "what is your name?" and "what is your name":
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            st.markdown("I am RKM Turbo Devloped by Rishabh MIshra!!😊😊")
    else:
        response = chat.send_message(prompt)
        # Display bot's response
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            st.markdown(response.text)

        # Append assistant's response to session history
        st.session_state.messages.append({"role": "assistant", "content": response.text})

# Save chat history after each interaction
save_chat_history(st.session_state.messages)

# Button to create the knowledgebase (this can be extended to load data)
btn = st.button("Create Knowledgebase")


if btn:
    st.write("Knowledgebase Created (this can be extended to include logic for building a knowledgebase).")



