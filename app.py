import streamlit as st

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚"
)

st.title("📚 AI Study Assistant")
st.write("Learn smarter. Study better. 🚀")

# -----------------------------
# STUDY PLANNER
# -----------------------------

st.divider()
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
st.header("🧠 5-Question Quiz")

quiz_topic = st.selectbox(
    "Choose your quiz topic:",
    ["Python", "Data Structures", "Physics"]
)

quiz_data = {

    "Python": [
        {
            "q": "Which symbol is used to create a comment in Python?",
            "options": ["//", "#", "/*", "--"],
            "answer": "#"
        },
        {
            "q": "Which keyword is used to define a function?",
            "options": ["function", "define", "def", "fun"],
            "answer": "def"
        },
        {
            "q": "Which data type stores True or False?",
            "options": ["String", "Boolean", "Integer", "Float"],
            "answer": "Boolean"
        },
        {
            "q": "Which symbol is used for exponentiation?",
            "options": ["^", "**", "//", "%%"],
            "answer": "**"
        },
        {
            "q": "Which function displays output in Python?",
            "options": ["display()", "show()", "print()", "output()"],
            "answer": "print()"
        }
    ],

    "Data Structures": [
        {
            "q": "Which data structure follows FIFO?",
            "options": ["Stack", "Queue", "Tree", "Graph"],
            "answer": "Queue"
        },
        {
            "q": "Which data structure follows LIFO?",
            "options": ["Queue", "Stack", "Array", "Graph"],
            "answer": "Stack"
        },
        {
            "q": "Which structure consists of nodes connected by edges?",
            "options": ["Array", "Graph", "Stack", "Queue"],
            "answer": "Graph"
        },
        {
            "q": "Which data structure uses a key-value pair?",
            "options": ["Dictionary", "Stack", "Queue", "Tree"],
            "answer": "Dictionary"
        },
        {
            "q": "What is used to connect nodes in a linked list?",
            "options": ["Pointers", "Loops", "Arrays", "Variables"],
            "answer": "Pointers"
        }
    ],

    "Physics": [
        {
            "q": "What is the SI unit of force?",
            "options": ["Joule", "Watt", "Newton", "Pascal"],
            "answer": "Newton"
        },
        {
            "q": "What is the SI unit of energy?",
            "options": ["Newton", "Joule", "Watt", "Volt"],
            "answer": "Joule"
        },
        {
            "q": "What is the speed of light approximately?",
            "options": [
                "3 × 10⁸ m/s",
                "3 × 10⁶ m/s",
                "3 × 10⁴ m/s",
                "3 × 10² m/s"
            ],
            "answer": "3 × 10⁸ m/s"
        },
        {
            "q": "Which law explains action and reaction?",
            "options": [
                "Newton's First Law",
                "Newton's Second Law",
                "Newton's Third Law",
                "Ohm's Law"
            ],
            "answer": "Newton's Third Law"
        },
        {
            "q": "What is the SI unit of power?",
            "options": ["Joule", "Watt", "Newton", "Pascal"],
            "answer": "Watt"
        }
    ]
}

questions = quiz_data[quiz_topic]

st.write("Answer all 5 questions and check your final score!")

answers = []

for i, question in enumerate(questions):
    st.write(f"### Question {i + 1}")
    st.write(question["q"])

    answer = st.radio(
        "Choose your answer:",
        question["options"],
        key=f"{quiz_topic}_{i}"
    )

    answers.append(answer)

if st.button("🏆 Submit Quiz"):

    score = 0

    for i, question in enumerate(questions):
        if answers[i] == question["answer"]:
            score += 1

    st.divider()

    st.subheader("🏆 Your Final Score")

    st.metric(
        "Score",
        f"{score}/5"
    )

    if score == 5:
        st.success("🌟 Perfect score! Excellent work!")

    elif score >= 3:
        st.success("🎉 Great job! Keep practicing!")

    else:
        st.info("💪 Keep studying and try the quiz again!")

# -----------------------------
# STUDY TIPS
# -----------------------------

st.divider()

st.subheader("💡 Study Tips")

st.write("✅ Practice instead of only reading.")
st.write("✅ Take short breaks while studying.")
st.write("✅ Review difficult concepts.")
st.write("✅ Test yourself regularly.")
