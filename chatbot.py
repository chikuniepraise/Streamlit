import streamlit as st

def generate_response(user_input):
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "how are you": "I'm just a program, so I don't have feelings, but thanks for asking! How can I help you?",
        "bye": "Goodbye! Have a great day!",
        "help": "Sure! I can assist you with information, answer questions, or just chat with you. What do you need help with?",
    }
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that. Can you please rephrase?")

st.title("Simple Chatbot")

if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

user_input = st.text_input("You: ", "", key="user_input")

if user_input:
    bot_response = generate_response(user_input)

    st.session_state["conversation"].append(f"You: {user_input}\nBot: {bot_response}\n")

st.write("\n".join(st.session_state["conversation"]))

if st.button("Clear Conversation"):
    st.session_state["conversation"] = []