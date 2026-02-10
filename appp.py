import os
import streamlit as st
import groq
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    groq_api_key = st.secrets["GROQ_API_KEY"]


#langsmithtracking
#langchain_api_key=os.getenv("LANGCHAIN_API_KEY")
#os.environ["LANGCHAIN_API_KEY"] = langchain_api_key

#os.environ["LANGCHAIN_TRACING"]="true"
#os.environ["LANGCHAIN_PROJECT"]="Q&A Chatbot With OPENAI"

# Prompt Template 
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user queries "),
        ("user","Question:{question}")
    ]
)
def generate_response(question,api_key,llm,temperature,max_tokens):
    groq.api_key=api_key
    llm=ChatGroq(model=llm)
    outputparser=StrOutputParser()
    chain=prompt|llm|outputparser
    answer=chain.invoke({'question':question})
    return answer

#Title of the app
st.title("Enhanced Q&A Chatbot With Groq")

#siebar settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your own AI api Key", type="password")

#DropDown
llm=st.sidebar.selectbox("Select and groq model",["meta-llama/llama-4-scout-17b-16e-instruct"])

# Adjust response parameter 
temperature = st.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.slider("MaxTokens",min_value=50,max_value=300,value=150)

# Main Interface for user input
st.write("Go ahead and ask any question")
user_input=st.text_input("You:")

if user_input:
    response = generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
elif user_input:
    st.warning("Please enter groq key")
else:
    st.write("Please provide the user input")        