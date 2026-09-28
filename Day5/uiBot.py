import ollama
import streamlit as st
st.set_page_config(page_title="Study Assistant", page_icon="📚")
st.title("📚 My Study Assistant")
st.markdown("### 🎓 Your personal AI learning partner")
if "messages" not in st.session_state:
    st.session_state.messages = []
with st.sidebar:
    st.header("⚙️ Chat Settings")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []

    personalities = {
        "👶 Kid": "Explain like a 5 year old in 2 simple lines.",
        "👨‍🏫 Teacher": "Answer like a teacher. Explain clearly in simple language.",
        "🤝 Friend": "Answer like a friendly classmate. Keep it simple and helpful.",
        "📚 Study Assistant": "You are a helpful study assistant. Give clear, accurate and exam-friendly answers."
    }
    personality = st.selectbox("🎭 Choose Personality",personalities.keys())
    uploaded_file = st.file_uploader("📄 Upload Study Notes",type=["txt"])
    if uploaded_file:
        try:
            context = uploaded_file.read().decode("utf-8")
            st.success("✅ File uploaded!")
            if st.button("👀 Display File"):
                st.text_area("📄 File Contents", context, height=200)
        except:
            st.error("❌ File is not supported")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
question = st.chat_input("💬 Ask your study question...")
if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })
    with st.chat_message("user"):
        st.markdown(question)
    messages = st.session_state.messages.copy()
    system_message = personalities[personality]
    if uploaded_file:
        system_message += (
            "\nUse the uploaded study notes to answer questions when relevant:\n"
            + context)
    messages.insert(0, {"role": "system","content": system_message})
    try:
        with st.spinner("🤔 Thinking..."):

            response = ollama.chat(
                model="llama3.2:3b",
                messages=messages
            )

        answer = response["message"]["content"]
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })
        with st.chat_message("assistant"):
            st.markdown(answer)
    except Exception as e:
        st.error("❌ Something went wrong!")