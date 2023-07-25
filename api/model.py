from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Chroma

# import os

# Set API key if running locally -- Commented out for Docker
# os.environ['OPENAI_API_KEY'] = ""


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


filepath = 'functionalsample.pdf'
custom_data = load_split_pdf(filepath)

embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(custom_data, embeddings)


memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
pdf_qa = ConversationalRetrievalChain.from_llm(OpenAI(temperature=0.3), retriever=vectorstore.as_retriever(),
                                               memory=memory)


def get_answer(question):
    return pdf_qa({"question": get_prompt(question)})["answer"]
