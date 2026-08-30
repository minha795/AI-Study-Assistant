import streamlit as st

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚"
)

st.title("📚 AI Study Assistant")
st.write("Learn smarter. Study better. 🚀")

st.divider()

# -----------------------------
# STUDY PLAN
# -----------------------------

st.header("🎯 Create Your Study Plan")

topic = st.text_input(
    "What do you want to study?",
    placeholder="Example: Python, Data Structures, Physics"
)

study_time = st.selectbox(
    "⏱️ How much time do you have?",
    ["30 minutes", "1 hour", "2 hours"]
)

difficulty = st.selectbox(
    "📊 Choose your level:",
    ["Beginner", "Intermediate", "Advanced"]
)

goal = st.selectbox(
    "🎯 What is your goal?",
    [
        "Understand the topic",
        "Prepare for an exam",
        "Practice questions"
    ]
)

if st.button("🚀 Generate My Study Plan"):

    if not topic.strip():
        st.warning("⚠️ Please enter a topic first.")

    else:
        st.success(f"🎉 Study plan created for **{topic}**!")

        st.write(f"**📚 Topic:** {topic}")
        st.write(f"**⏱️ Time:** {study_time}")
        st.write(f"**📊 Level:** {difficulty}")
        st.write(f"**🎯 Goal:** {goal}")

        st.subheader("📝 Recommended Study Plan")

        if study_time == "30 minutes":
            plan = [
                "🧠 10 min — Learn the basic concepts",
                "📝 10 min — Make short notes",
                "❓ 10 min — Practice questions"
            ]

        elif study_time == "1 hour":
            plan = [
                "🧠 20 min — Learn the core concepts",
                "📝 15 min — Make notes",
                "💡 15 min — Study examples",
                "❓ 10 min — Practice questions"
            ]

        else:
            plan = [
                "🧠 30 min — Learn the fundamentals",
                "📝 20 min — Create detailed notes",
                "💡 30 min — Study examples",
                "❓ 20 min — Practice questions",
                "🔄 20 min — Revise"
            ]

        for item in plan:
            st.write(item)

# -----------------------------
# QUIZ
# -----------------------------

st.divider()

st.header("🧠 Quick Quiz")

quiz_topic = st.selectbox(
    "Choose a quiz topic:",
    ["Python", "Data Structures", "Physics"]
)

questions = {
    "Python": {
        "question": "Which symbol is used to create a comment in Python?",
        "options": ["//", "#", "/*", "--"],
        "answer": "#"
    },

    "Data Structures": {
        "question": "Which data structure follows FIFO?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue"
    },

    "Physics": {
        "question": "What is the SI unit of force?",
        "options": ["Joule", "Watt", "Newton", "Pascal"],
        "answer": "Newton"
    }
}

quiz = questions[quiz_topic]

st.write(f"**{quiz['question']}**")

answer = st.radio(
    "Choose your answer:",
    quiz["options"]
)

if st.button("✅ Check Answer"):

    if answer == quiz["answer"]:
        st.success("🎉 Correct! Great job!")

        st.session_state.score = st.session_state.get(
            "score", 0
        ) + 1

    else:
        st.error(
            f"❌ Not quite. The correct answer is **{quiz['answer']}**."
        )

# -----------------------------
# SCORE
# -----------------------------

if "score" in st.session_state:

    st.divider()

    st.subheader("🏆 Your Progress")

    st.metric(
        label="Quiz Score",
        value=st.session_state.score
    )

    if st.session_state.score >= 3:
        st.success("🌟 Excellent work!")

    elif st.session_state.score >= 1:
        st.info("💪 Keep practicing!")

    else:
        st.info("📚 Keep learning and try again!")

# -----------------------------
# STUDY TIPS
# -----------------------------

st.divider()

st.subheader("💡 Study Tips")

st.write("✅ Practice instead of only reading.")
st.write("✅ Take short breaks while studying.")
st.write("✅ Review difficult concepts again.")
st.write("✅ Test yourself with questions.")
