from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain.messages import HumanMessage,AIMessage
from langchain.agents import create_agent
from langchain.tools import tool
import streamlit as st




st.title("Basic chat bot with a weather tool")
if "history" not in st.session_state:
    st.session_state.history = []
history = st.session_state.history


def weatherTool(city:str)->str:
    """
    This function is a tool that can be used to get information about the weather.
    """
    return f"It's sunny today in {city}"

llm = OllamaLLM(model="qwen3")


agent = create_agent(
    model="ollama:qwen3",
    system_prompt="You are a helpful assistant that knows everything",
    tools=[weatherTool],
)

st.text("Hello, I am a helpfull assistant and I can answer your questions")
userText = st.text_input("Enter your Question")

if userText:
    history.append({"role": "user", "content": f"{userText}"})
    response = agent.invoke({"messages":history})
    history.append({"role": "assistant", "content": f"{response}"})

    st.write(response["messages"][-1].content)
    print(response["messages"][-1].content)



