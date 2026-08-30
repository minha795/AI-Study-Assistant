import streamlit as st

# Page settings
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚"
)

# Title
st.title("📚 AI Study Assistant")
st.write("Learn smarter. Study better. 🚀")

st.divider()

# Topic input
st.header("🎯 Choose a topic")

topic = st.text_input(
    "Enter a subject or topic:",
    placeholder="Example: Python, Data Structures, Physics"
)

# Study content
study_data = {
    "python": {
        "explanation": "Python is a beginner-friendly programming language used for web development, automation, data science, and artificial intelligence.",
        "plan": [
            "Learn variables and data types",
            "Learn if-else statements",
            "Learn loops",
            "Learn functions",
            "Practice small programs"
        ],
        "questions": [
            "What is a variable in Python?",
            "What is the difference between a list and a tuple?",
            "What is a for loop used for?"
        ]
    },

    "data structures": {
        "explanation": "Data structures are ways of organizing and storing data so that it can be used efficiently.",
        "plan": [
            "Learn arrays and lists",
            "Learn stacks and queues",
            "Learn linked lists",
            "Learn trees",
            "Learn graphs"
        ],
        "questions": [
            "What is a stack?",
            "What is a queue?",
            "What is the difference between an array and a linked list?"
        ]
    },

    "physics": {
        "explanation": "Physics is the study of matter, energy, motion, forces, and how objects interact with each other.",
        "plan": [
            "Understand the basic concepts",
            "Learn important formulas",
            "Study solved examples",
            "Practice numerical problems",
            "Review mistakes"
        ],
        "questions": [
            "What is force?",
            "What is the difference between speed and velocity?",
            "What is Newton's second law?"
        ]
    }
}

# Button
if st.button("🚀 Start Studying"):

    if not topic.strip():
        st.warning("⚠️ Please enter a subject or topic.")

    else:
        topic_key = topic.lower().strip()

        # Use prepared content if available
        if topic_key in study_data:
            data = study_data[topic_key]

            st.success(f"🎉 Study session started for **{topic}**!")

            st.subheader("🧠 Quick Explanation")
            st.write(data["explanation"])

            st.subheader("📝 Study Plan")

            for number, item in enumerate(data["plan"], start=1):
                st.write(f"**{number}.** {item}")

            st.subheader("❓ Practice Questions")

            for number, question in enumerate(data["questions"], start=1):
                st.write(f"**{number}.** {question}")

            st.info("💡 Tip: Study one step at a time and practice what you learn.")

        else:
            st.success(f"🎉 Study session started for **{topic}**!")

            st.subheader("📚 General Study Plan")

            st.write("**1. 🧠 Understand**")
            st.write(f"Learn the basic concepts of {topic}.")

            st.write("**2. 📝 Take Notes**")
            st.write(f"Write down the important points about {topic}.")

            st.write("**3. 💻 Practice**")
            st.write(f"Practice questions and examples related to {topic}.")

            st.write("**4. 🔄 Review**")
            st.write(f"Revise the important concepts of {topic}.")

            st.subheader("❓ Practice Questions")

            st.write(f"1. What is {topic}?")
            st.write(f"2. What are the important concepts of {topic}?")
            st.write(f"3. Where is {topic} used?")

            st.info("💡 More topics and AI-powered features can be added next!")
