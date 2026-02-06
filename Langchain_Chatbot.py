import os
import streamlit as st
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

# Replace with your OpenAI API key
api = "your-openai-api-key-here"
os.environ["OPENAI_API_KEY"] = api

st.title("LangChain Chatbot")

# keeps track of conversation history in session state
if "history" not in st.session_state:
    st.session_state.history = []

# Sample questions for testing
st.sidebar.header("Sample Questions")
sample_queries = [
    "How to remove the filter from an AC?",
    "How do I know when an avocado is ripe?",
    "What is the difference between baking soda and baking powder?",
    "Why do cats purr?",
    "What is the world's fastest bird?"
]

# Display sample questions in sidebar
for i, query in enumerate(sample_queries, 1):
    st.sidebar.markdown(f"**{i}.** {query}")

# Prompt template with placeholders for question and conversation history
qa_template = PromptTemplate(
    input_variables=["question", "history"],
    template="""
Answer the questions clearly and concisely.

Previous conversation:
{history}

User question: {question}

Answer:
"""
)

# LLM 
llm = OpenAI()

# Chain
qa_chain = qa_template | llm

# Sidebar for running the sample tests
if st.sidebar.button("Run Sample Questions"):
    st.sidebar.markdown("---")
    for q in sample_queries:
        result = qa_chain.invoke({
            "question": q,
            "history": ""
        })
        st.sidebar.markdown(f"**Q:** {q}")
        st.sidebar.markdown(f"**A:** {result}")
        st.sidebar.markdown("---")

# User input
prompt_input = st.text_input("Enter your question:")

# Run the chain with user input and conversation history
if prompt_input:
    history_text = "\n".join(st.session_state.history) if st.session_state.history else "None"

    response = qa_chain.invoke({
        "question": prompt_input,
        "history": history_text
    })

    # Saving to memory
    st.session_state.history.append(f"User: {prompt_input}")
    st.session_state.history.append(f"AI: {response}")

    st.subheader("Answer")
    st.write(response)

# View the conversation history
with st.expander("Conversation History"):
    if st.session_state.history:
        for entry in st.session_state.history:
            st.write(entry)
    else:
        st.info("No conversation yet.")

# Clear history button
if st.button("Clear History"):
    st.session_state.history = []
    st.rerun()