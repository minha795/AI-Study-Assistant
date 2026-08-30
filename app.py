import streamlit as st

# Page settings
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="centered"
)

# Title
st.title("📚 AI Study Assistant")
st.write("Your personal study companion 🤖")

st.divider()

# Topic input
st.header("🎯 What do you want to study?")

topic = st.text_input(
    "Enter a subject or topic:",
    placeholder="Example: Python, Data Structures, Linear Algebra"
)

# Button
if st.button("🚀 Start Studying"):
    if topic.strip():
        st.success(f"Great! Let's study **{topic}**!")

        st.subheader("📖 Your Study Session")

        st.write(f"### 🔹 Topic: {topic}")

        st.write("**1. 🧠 Understand the basics**")
        st.write(f"Learn the basic concepts of **{topic}**.")

        st.write("**2. 📝 Take notes**")
        st.write(f"Write down the important points about **{topic}**.")

        st.write("**3. 💡 Practice**")
        st.write(f"Try some practice questions related to **{topic}**.")

        st.write("**4. ✅ Review**")
        st.write(f"Review what you learned about **{topic}**.")

        st.info("🎉 Your study session has started!")

    else:
        st.warning("⚠️ Please enter a subject or topic first.")
