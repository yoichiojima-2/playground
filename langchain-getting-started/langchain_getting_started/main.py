import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# load api key
load_dotenv()
assert os.getenv("OPENAI_API_KEY")

# instanciate model
model = ChatOpenAI(model="gpt-4o-mini")

# build messages
message =[
    SystemMessage(content="you are a translator who translate english to japanese"),
    HumanMessage(content="hello")
]

# api call
res = model.invoke(message)

# display response
from pprint import pprint
pprint(res)