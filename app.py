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

# App framework
st.title("Top 10 Statistics 🥇🏆")
category = st.text_input("Type a category:")
parameter = st.text_input("Type a parameter to rank your category:")


# Prompt templates
stats_template = PromptTemplate(
    input_variables=["category", "parameter"],
    template="Write the top 10 {category} based on {parameter} and format the output as a numerical list and mention the numerical values(if any) for each rank",
)

# script_template = PromptTemplate(
#     input_variables=["title", "wikipedia_research"],
#     template="write me a youtube video script based on this title TITLE: {title} while leveraging this wikipedia reserch:{wikipedia_research} ",
# )

comparison_template = PromptTemplate(
    input_variables=["stats", "wikipedia_research"],
    template="Predict by when can #2 overtake #1 in this list: {stats}, leveraging this wikipedia research- {wikipedia_research}",
)
comparison_template = PromptTemplate(
    input_variables=["stats", "wikipedia_research"],
    template="Predict by when can #2 overtake #1 in this list: {stats}{wikipedia_research}",
)

# Memory
# title_memory = ConversationBufferMemory(input_key="topic", memory_key="chat_history")
# script_memory = ConversationBufferMemory(input_key="title", memory_key="chat_history")

# Llms
llm = OpenAI(temperature=0.9)
stats_chain = LLMChain(
    llm=llm,
    prompt=stats_template,
    verbose=True,
    output_key="stats",
    # memory=title_memory,
)
compare_chain = LLMChain(
    llm=llm,
    prompt=comparison_template,
    verbose=True,
    output_key="result",
    # memory=script_memory,
)

wiki = WikipediaAPIWrapper()
retriever = WikipediaRetriever()


# Show stuff to the screen if there's a prompt
if parameter and category:
    stats = stats_chain.run({"parameter": parameter, "category": category})
    wiki_prompt = f"{category} rankings by {parameter}"
    # wiki_research = wiki.run(wiki_prompt)
    # wiki_research = retriever.get_relevant_documents(query=wiki_prompt)[0].page_content

    result = compare_chain.run(stats=stats, wikipedia_research="")

    st.write(stats)
    st.write(result)
    # st.write(wiki_research)
