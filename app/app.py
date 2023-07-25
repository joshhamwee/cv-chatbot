import os

import streamlit as st
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Chroma

# Set API key
os.environ['OPENAI_API_KEY'] = ""


# Prompt template to ensure it responds to the user's question in first person/as "ME"
def get_prompt(question):
    return f"""Answer the following question as if you are John Smith, ie in first person.
    Follow Up Input: {question}"""


# Load PDF and split into sections
def load_split_pdf(filepath: str):
    try:
        loader = PyPDFLoader(filepath)
        return loader.load_and_split()
    except Exception as e:
        print(e)
        return None


# APP Customisations
st.set_page_config(layout="wide")
with st.sidebar:
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"


filepath = 'functionalsample.pdf'
custom_data = load_split_pdf(filepath)

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(custom_data, embeddings)


memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
pdf_qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0.3), retriever=vectorstore.as_retriever(),
                                               memory=memory)

st.title('File Chatbot')

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = pdf_qa({"question": get_prompt(prompt)})
    msg = response["answer"]
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
