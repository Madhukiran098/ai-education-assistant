from backend.llm.client import llm_client
from backend.memory.memory_manager import memory_manager

class PlanningAgent:
    def __init__(self):
        self.name = "PlanningAgent"
        self.role = "Senior Project Planner - BFSI Domain"

    def execute(self, business_request: str) -> dict:
        print(f"[{self.name}] Planning for: {business_request}")
        
        prompt = f"""
        Business Request: {business_request}
        Task: Create a detailed enterprise execution plan.
        Include: 1. Intent analysis 2. 5-step workflow 3. Risk factors 4. Success criteria
        Format: JSON style structured output.
        """
        
        llm_response = llm_client.generate(prompt, self.name)
        
        plan_output = {
            "intent": business_request,
            "role": self.role,
            "workflow_steps": ["research", "analyze", "evaluate", "decide", "execute"],
            "risks": ["data_privacy", "compliance"],
            "llm_output": llm_response,
            "status": "planned"
        }
        
        memory_manager.add_short(self.name, plan_output)
        memory_manager.add_long("current_plan", plan_output)
        
        return plan_output
