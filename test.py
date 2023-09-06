# Bring in deps
import os
from keys import openai_api_key

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper
from langchain.retrievers import WikipediaRetriever

os.environ["OPENAI_API_KEY"] = openai_api_key

wiki = WikipediaAPIWrapper()
# retriever = WikipediaRetriever()


try:
    wiki_prompt = "1. Shahrukh khan - Net Worth: 600 Million"
    wiki_research = wiki.run(wiki_prompt)
except Exception as e:
    print("Error prompting wiki, skipping-", e)
    wiki_research = ""
    # wiki_res
print(wiki_prompt, "\n", wiki_research)
