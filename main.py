import streamlit as st
import google.generativeai as ai
import os
import uuid

# Configure the API key
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
ai.configure(api_key=API_KEY)

# Initialize the chat model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

st.title("RKM Turbo")
st.subheader("How can I help you with?")

USER_AVATAR = "👤"
BOT_AVATAR = "🤖"

# Generate a unique session ID for each user
if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())
    st.session_state["messages"] = []  # Initialize a fresh chat history for the new user

# Sidebar options
with st.sidebar:
    if st.button("🗑️ delete history"):
        st.session_state["messages"] = []  # Reset chat history for the current user
    st.link_button("LinkedIn", "https://www.linkedin.com/in/rkmisntexist/")
    st.link_button("Github", "https://github.com/rkm0078")

# Display chat history for the current user
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
    if prompt.lower() in [
        "who are you",
        "what's your name",
        "what is your name?",
    ]:
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            st.markdown("I am RKM Turbo developed by Rishabh Mishra! 😊😊")
    else:
        response = chat.send_message(prompt)
        # Display bot's response
        with st.chat_message("assistant", avatar=BOT_AVATAR):
            st.markdown(response.text)

        # Append assistant's response to session history
        st.session_state.messages.append({"role": "assistant", "content": response.text})

# Button to create the knowledgebase (this can be extended to load data)
btn = st.button("Create Knowledgebase")
if btn:
    st.write("Knowledgebase Created (this can be extended to include logic for building a knowledgebase).")
