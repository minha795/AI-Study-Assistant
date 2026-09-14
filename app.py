# -----------------------------
# SMART NOTES GENERATOR
# -----------------------------

st.divider()
st.header("📝 Smart Notes Generator")

notes_topic = st.text_input(
    "Enter a topic to get quick notes:",
    placeholder="Example: Python Functions"
)

notes_level = st.selectbox(
    "Choose your level:",
    ["Beginner", "Intermediate", "Advanced"],
    key="notes_level"
)

if st.button("📝 Generate Notes"):

    if not notes_topic.strip():
        st.warning("⚠️ Please enter a topic first.")

    else:
        st.success(f"📚 Notes created for **{notes_topic}**!")

        st.subheader(f"📖 {notes_topic}")

        st.write("### 🔹 Definition")
        st.write(
            f"{notes_topic} is an important concept that helps students "
            f"understand the fundamentals of the subject."
        )

        st.write("### 🔹 Key Points")
        st.write("• Understand the basic concepts.")
        st.write("• Learn the important terms and definitions.")
        st.write("• Study simple examples.")
        st.write("• Practice questions related to the topic.")

        st.write("### 🔹 Example")
        st.code(
            f"# Example related to {notes_topic}\n"
            f"print('Learning {notes_topic}')",
            language="python"
        )

        st.write("### 🔹 Quick Revision")
        st.info(
            f"💡 Remember the definition, key concepts, examples, "
            f"and applications of {notes_topic}."
        )
