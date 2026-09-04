import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class LLMClient:
    def __init__(self):
        # OpenAI API key from env
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.3,
            api_key=os.getenv("OPENAI_API_KEY")
        )
    
    def generate(self, prompt: str, agent_name: str = "") -> str:
        system_msg = f"You are {agent_name}, an enterprise AI agent. Be precise and professional."
        human_msg = prompt
        
        template = ChatPromptTemplate.from_messages([
            ("system", system_msg),
            ("human", "{input}")
        ])
        chain = template | self.llm
        response = chain.invoke({"input": human_msg})
        return response.content

llm_client = LLMClient()
