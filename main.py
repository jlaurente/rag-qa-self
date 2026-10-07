import streamlit as st
from langchain_helper import execute_user_query


st.set_page_config(
    page_title="DPA Chatbot - Data Privacy Act of 2012",
    page_icon="🛡️",
    layout="centered",
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #eff6ff 100%);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 28px;
        padding: 32px 28px;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
    ">
        <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 8px;">
            <div style="
                width: 56px; height: 56px;
                background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
                border-radius: 20px;
                display: flex; align-items: center; justify-content: center;
                font-size: 28px;
                color: white;
                box-shadow: 0 4px 12px rgba(59, 130, 246, 0.35);
            ">🛡️</div>
            <div>
                <h1 style="margin: 0; font-size: 26px; font-weight: 700; color: #0f172a;">
                    Data Privacy Act of 2012
                </h1>
                <p style="margin: 4px 0 0 0; font-size: 14px; color: #64748b;">
                    Republic Act No. 10173 · Philippine Data Protection Law
                </p>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.expander("📚 Quick Guide — What you can ask", expanded=False):
    st.markdown(
        """
        - **Scope & Coverage**: *"Who is covered by the Data Privacy Act?"*
        - **Rights of Data Subjects**: *"What are my rights as a data subject under the DPA?"*
        - **Data Processing Principles**: *"What principles must be followed when processing personal data?"*
        - **Consent Requirements**: *"When is consent required for data processing?"*
        - **Penalties & Fines**: *"What are the penalties for violating the Data Privacy Act?"*
        - **National Privacy Commission**: *"What is the role of the NPC?"*
        - **Sensitive Personal Information**: *"How is sensitive personal information protected?"*
        """
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.chat_message(
    "assistant",
    avatar="🛡️"
):
    st.markdown(
        "Hello! I'm your **Data Privacy Act (DPA) Assistant**. "
        "I can answer questions about **Republic Act No. 10173** — the Philippine Data Privacy Act of 2012. "
        "Ask me anything about data protection rights, obligations, penalties, and compliance requirements. 👋"
    )

for message in st.session_state.messages:
    with st.chat_message(
        message["role"],
        avatar="👤" if message["role"] == "user" else "🛡️"
    ):
        st.markdown(message["content"])

if query_text := st.chat_input("Ask a question about the Data Privacy Act of 2012..."):
    with st.chat_message("user", avatar="👤"):
        st.markdown(query_text)
    st.session_state.messages.append({"role": "user", "content": query_text})

    with st.chat_message("assistant", avatar="🛡️"):
        with st.spinner("📖 Reviewing the Data Privacy Act..."):
            try:
                response = execute_user_query(query_text)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                friendly = (
                    "😕 Something unexpected happened while processing your question. "
                    "Please refresh the page and try again in a few moments."
                )
                st.error(friendly, icon="⚠️")
                st.session_state.messages.append({"role": "assistant", "content": friendly})
