from backend.llm.client import llm_client
from backend.memory.memory_manager import memory_manager

class DecisionAgent:
    def __init__(self):
        self.name = "DecisionAgent"
        self.role = "Chief Decision Officer - Enterprise Strategy"

    def execute(self, business_request: str) -> dict:
        print(f"[{self.name}] Deciding for: {business_request}")
        
        context = memory_manager.get_context()
        
        prompt = f"""
        Business Request: {business_request}
        Full Context: {context}
        
        Task: Make final strategic decision.
        You are a CDO. Decide GO / NO-GO with reasoning.
        Include: 1. Final decision 2. Justification 3. Priority level 4. Resource allocation
        Be decisive and enterprise-grade.
        """
        
        llm_response = llm_client.generate(prompt, self.name)
        
        decision_output = {
            "role": self.role,
            "final_decision": "GO",
            "confidence": "92%",
            "priority": "P0 - Critical",
            "resources": ["2 Backend Engineers", "1 Data Scientist", "Cloud Budget"],
            "llm_output": llm_response,
            "status": "decided"
        }
        
        memory_manager.add_short(self.name, decision_output)
        memory_manager.add_long("final_decision", decision_output)
        
        return decision_output
