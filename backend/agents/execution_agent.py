from backend.llm.client import llm_client
from backend.memory.memory_manager import memory_manager

class ExecutionAgent:
    def __init__(self):
        self.name = "ExecutionAgent"
        self.role = "Execution Lead - Implementation & Delivery"

    def execute(self, business_request: str) -> dict:
        print(f"[{self.name}] Executing: {business_request}")
        
        context = memory_manager.get_context()
        
        prompt = f"""
        Business Request: {business_request}
        Full Memory Context: {context}
        
        Task: Create final execution report and next steps.
        Include: 1. Implementation roadmap (30-60-90 days) 2. Deliverables 3. Team assignments 4. Success metrics
        This is the final output user will see.
        """
        
        llm_response = llm_client.generate(prompt, self.name)
        
        execution_output = {
            "role": self.role,
            "roadmap": "30 days: MVP, 60 days: Beta, 90 days: Production",
            "deliverables": ["API", "Dashboard", "Compliance Report"],
            "final_summary": llm_response,
            "status": "executed"
        }
        
        memory_manager.add_short(self.name, execution_output)
        
        # Combine all for final result
        final_result = {
            "business_request": business_request,
            "memory_trace": memory_manager.get_context(),
            "final_output": execution_output
        }
        
        return final_result
