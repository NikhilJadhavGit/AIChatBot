from langchain_ollama import OllamaLLM
from langchain.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
import streamlit as st
#from langchain_core import

st.title("Basic chat bot with manual chat history")
messages = [
    SystemMessage(content="You are a helpful assistant that knows everything"),
    MessagesPlaceholder(variable_name="history",optional=True),
    ("human","{question}")
]
prompt = ChatPromptTemplate.from_messages(messages)
llm = OllamaLLM(model="qwen3", temperature=0.5, max_tokens=1024)
chain = prompt|llm
if "history" not in st.session_state:
    st.session_state.history = []
history=st.session_state.history

st.text("Hello, I am a helpfull assistant and I can answer your questions")
userText = st.text_input("Enter your Question")




# Pass input as an argument to the llm.invoke method

if userText:
    response = chain.invoke({"history":history,"question":userText})
    history.extend([HumanMessage(content=userText),AIMessage(content=response)])
    st.text(response)