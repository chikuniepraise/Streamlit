import streamlit as st

def generate_response(user_input):
    departments = {
        "reception": "The Reception is located on the Ground Floor.",
        "it support": "The IT Support is located on the Seventh Floor.",
        "human resources": "The Human Resources department is located on the First Floor.",
        "finance department": "The Finance Department is located on the First Floor.",
        "marketing department": "The Marketing Department is located on the Second Floor.",
        "sales department": "The Sales Department is located on the Second Floor.",
        "research and development": "The Research and Development department is located on the Third Floor.",
        "legal department": "The Legal Department is located on the Third Floor."
    }
    
    user_input = user_input.lower()
    
    return departments.get(user_input, "I'm sorry, I don't have information about that department. Please provide a valid department name.")

st.title("Office Directory Chatbot")

if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

user_input = st.text_input("You: ", "", key="user_input")

if user_input:
    bot_response = generate_response(user_input)

    st.session_state["conversation"].append(f"You: {user_input}")
    st.session_state["conversation"].append(f"Bot: {bot_response}")

st.write("\n".join(st.session_state["conversation"]))

if st.button("Clear Conversation"):
    st.session_state["conversation"] = []

