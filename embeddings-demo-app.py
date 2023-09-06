import os
import sys
import streamlit as st

# import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

from keys import openai_api_key

os.environ["OPENAI_API_KEY"] = openai_api_key
# Enable to save to disk & reuse the model (for repeated queries on the same data)
PERSIST = False

query = None
if len(sys.argv) > 1:
    query = sys.argv[1]

if PERSIST and os.path.exists("persist"):
    print("Reusing index...\n")
    vectorstore = Chroma(
        persist_directory="persist", embedding_function=OpenAIEmbeddings()
    )
    index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
    # loader = TextLoader(
    #     r"C:\Users\Mohit Khanwale\Documents\Work\Data-Axle\lang-chain-project\data\data.txt"
    # )  # Use this line if you only need data.txt
    loader = DirectoryLoader("data/")
    if PERSIST:
        index = VectorstoreIndexCreator(
            vectorstore_kwargs={"persist_directory": "persist"}
        ).from_loaders([loader])
    else:
        index = VectorstoreIndexCreator().from_loaders([loader])

retrieval_chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)
st.title("Retrieval App 🔎🕵")
query = st.text_input("Prompt for your personal data:")
chat_history = []
# while True:
#     if not query:
#         query = input("Prompt: ")
#     if query in ["quit", "q", "exit"]:
#         sys.exit()
#     result = retrieval_chain({"question": query, "chat_history": chat_history})
#     print(result["answer"])

#     chat_history.append((query, result["answer"]))
#     query = None

result = retrieval_chain({"question": query, "chat_history": chat_history})
print(result["answer"])
st.write(result["answer"])
