# Bring in deps
import os
from keys import openai_api_key, serp_api_key

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType

from langchain.chat_models import ChatOpenAI

# from langchain.memory import ConversationBufferMemory
# from langchain.retrievers import WikipediaRetriever

os.environ["SERPAPI_API_KEY"] = serp_api_key
os.environ["OPENAI_API_KEY"] = openai_api_key

# App framework
st.title("Top 10 Statistics 🥇🏆")
category = st.text_input("Type a category:")
parameter = st.text_input("Type a parameter to rank your category:")


# Llms
# llm = OpenAI(temperature=0.7)
llm_model = "gpt-3.5-turbo"
llm = ChatOpenAI(temperature=0, model=llm_model)
tools = load_tools(["serpapi", "wikipedia"], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose=True,
    max_iterations=3,
    early_stopping_method="generate",
)

# Show stuff to the screen if there's a prompt
if parameter and category:
    # stats = stats_chain.run({"parameter": parameter, "category": category})
    prompt = f"""
    List the top 10 {category} based on {parameter} and give quantitative values for each rank.    
    """
    output = agent(prompt)

    st.write(output["output"])
