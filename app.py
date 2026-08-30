import streamlit as st

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚"
)

st.title("📚 AI Study Assistant")
st.write("Learn smarter. Study better. 🚀")

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
    ["Understand the topic", "Prepare for an exam", "Practice questions"]
)

if st.button("🚀 Generate My Study Plan"):

    if not topic.strip():
        st.warning("⚠️ Please enter a topic first.")

    else:
        st.success(f"🎉 Study plan created for **{topic}**!")

        st.subheader("📋 Your Study Details")

        st.write(f"**📚 Topic:** {topic}")
        st.write(f"**⏱️ Available time:** {study_time}")
        st.write(f"**📊 Level:** {difficulty}")
        st.write(f"**🎯 Goal:** {goal}")

        st.divider()

        st.subheader("📝 Recommended Study Plan")

        if study_time == "30 minutes":
            plan = [
                "🧠 10 min — Learn the basic concepts",
                "📝 10 min — Write important notes",
                "❓ 10 min — Practice questions"
            ]

        elif study_time == "1 hour":
            plan = [
                "🧠 20 min — Learn the core concepts",
                "📝 15 min — Make short notes",
                "💡 15 min — Study examples",
                "❓ 10 min — Practice questions"
            ]

        else:
            plan = [
                "🧠 30 min — Learn the fundamentals",
                "📝 20 min — Create detailed notes",
                "💡 30 min — Study examples",
                "❓ 20 min — Practice questions",
                "🔄 20 min — Revise everything"
            ]

        for item in plan:
            st.write(item)

        st.divider()

        st.subheader("💡 Study Tips")

        st.write("✅ Keep your phone away while studying.")
        st.write("✅ Take short breaks between study sessions.")
        st.write("✅ Practice instead of only reading.")
        st.write("✅ Review what you learned before finishing.")

        st.info(
            "🌟 Tip: Consistent small study sessions are better "
            "than trying to learn everything at once."
)
