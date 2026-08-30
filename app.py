import streamlit as st

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚"
)

st.title("📚 AI Study Assistant")
st.write("Your personal study companion 🤖")

st.header("What do you want to study?")

topic = st.text_input("Enter a subject or topic:")

if st.button("Start Studying"):
    if topic:
        st.success(f"Great! Let's learn about **{topic}** 🚀")
    else:
        st.warning("Please enter a topic first.")
