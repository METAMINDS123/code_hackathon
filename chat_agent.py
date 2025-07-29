from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Initialize your LLM
def get_chat_agent():
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)
    memory = ConversationBufferMemory()
    conversation = ConversationChain(llm=llm, memory=memory, verbose=True)
    return conversation
