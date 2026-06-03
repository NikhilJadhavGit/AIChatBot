from langchain_ollama import OllamaLLM
from langchain.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
#from langchain_core import
messages = [
    SystemMessage(content="You are a helpful assistant that knows everything,Before anything, use wink emoji befor and then please answer user's questions"),
    MessagesPlaceholder(variable_name="history",optional=True),
    ("human","{question}")
]
# prompt = ChatPromptTemplate.from_messages([("system","Please answer the user's questions:"),
#                                            ("human","{user_input}")])
prompt = ChatPromptTemplate.from_messages(messages)

llm = OllamaLLM(model="qwen3", temperature=0.5, max_tokens=1024)
chain = prompt|llm

# Pass input as an argument to the llm.invoke method
history=[]
question1 = "I want you to remember that my name is Nikhil and I am 27 years old"
response = chain.invoke({"question":question1})
history.extend([HumanMessage(content=question1),AIMessage(content=response)])

print(response)

response = chain.invoke({"history":history,"question":"What is my name?"})

print(response)