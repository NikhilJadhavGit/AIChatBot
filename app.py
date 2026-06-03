
from langchain.agents import create_agent
import streamlit as st


st.title("Basic chat bot with a weather tool")


st.text("Hello, I am a helpfull assistant and I can answer your questions")
userText = st.text_input("Enter your Question")

def weatherTool(city:str)->str:
    """
    This function is a tool that can be used to get information about the weather.
    """
    return f"It's sunny today in {city}"

agent = create_agent(
    model="ollama:qwen3",
    system_prompt="You are a helpful agent who answers the user's question",
    tools=[weatherTool]
)

if userText:
    response=agent.invoke(
        {"messages": [{"role": "user", "content": f"{userText}"}]}
    )
    print(response)
    st.write(response.content())






# Set page configuration
# st.set_page_config(page_title="AI ChatBot", layout="wide")

# # Title
# st.title("AI ChatBot")

