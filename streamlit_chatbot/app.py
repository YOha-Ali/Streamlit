import streamlit as st
import google.generativeai as genai
import os
from datetime import datetime
# from hello_config import config 

from dotenv import load_dotenv
load_dotenv() 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to get Gemini response
def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content(prompt)
    return response.text

def main():
    st.set_page_config(page_title="AI Chatbot by YOha", layout="centered")

    st.markdown("<h1 style='text-align: center;'>֎ AI Chatbot 🤖</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>✧˖°By YOha Ali Azam✧˖°</h3>", unsafe_allow_html=True)

    # Chatbot personality selector (simple example)
    personality = st.sidebar.selectbox(
        "Select Chatbot Personality",
        ("Friendly", "Formal", "Humorous", "Horror")
    )
    st.sidebar.write(f"Current personality: {personality}")

    # Initialize all conversations (list of past chats)
    if "all_conversations" not in st.session_state:
        st.session_state.all_conversations = []

    # Initialize current chat messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Clear Chat = Save current chat + start a new one
    if st.sidebar.button("Clear Chat (New Conversation)"):
        if st.session_state.messages:
            st.session_state.all_conversations.append(st.session_state.messages)
        st.session_state.messages = [] 
        st.session_state.current_prompt_behavior = ""
        st.rerun() 

    # Sidebar: Show all past saved conversations
    st.sidebar.markdown("### 📁 Saved Conversations")

    if st.session_state.all_conversations:
        for idx, convo in enumerate(st.session_state.all_conversations, start=1):
            preview = convo[0]["content"][:30]  # First message preview
            with st.sidebar.expander(f"💬 Conversation {idx}: {preview}"):
                # Show full conversation inside the expander
                for msg in convo:
                    role = "🧑 You" if msg["role"] == "user" else "🤖 Bot"
                    st.write(f"**{role}:** {msg['content']}")
    else:
        st.sidebar.write("No saved conversations yet.")

    # Initialize behavior instructions
    if "current_prompt_behavior" not in st.session_state:
        st.session_state.current_prompt_behavior = ""

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask me Anything dude...❤"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Prepare full prompt for Gemini, including personality
        behavior_instruction = f"Befriendly and respond like a {personality} chatbot."
        
        # Only prepend behavior instruction if it's new or changed for this session
        if st.session_state.current_prompt_behavior != behavior_instruction:
            full_gemini_prompt = f"{behavior_instruction}\n\n{prompt}"
            st.session_state.current_prompt_behavior = behavior_instruction
        else:
            full_gemini_prompt = prompt

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            # Simulate streaming or direct call to Gemini
            with st.spinner("Thinking..."):
                gemini_response = get_gemini_response(full_gemini_prompt)
                full_response = gemini_response

            # Add timestamp
            timestamp = datetime.now().strftime("%I:%M %p")

            # Python-only Markdown styling (no HTML errors)
            styled_response = f"**{full_response}**  \n\n*{timestamp}*"
            message_placeholder.markdown(styled_response)

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": styled_response})
if __name__ == "__main__":
    main()
