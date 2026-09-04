from backend.llm.client import llm_client
from backend.memory.memory_manager import memory_manager

class ResearchAgent:
    def __init__(self):
        self.name = "ResearchAgent"
        self.role = "Enterprise Research Specialist - Market & Compliance"

    def execute(self, business_request: str) -> dict:
        print(f"[{self.name}] Researching: {business_request}")
        
        # Get context from memory
        context = memory_manager.get_context()
        
        prompt = f"""
        Business Request: {business_request}
        Previous Plan: {context.get('long_term', {}).get('current_plan', 'N/A')}
        
        Task: Conduct deep research.
        Include: 1. Market trends 2. Regulatory requirements (BFSI) 3. Competitor analysis 4. Data sources needed
        Be specific and actionable.
        """
        
        llm_response = llm_client.generate(prompt, self.name)
        
        research_output = {
            "role": self.role,
            "market_insights": "BFSI digital transformation trends",
            "compliance_needs": ["GDPR", "PCI-DSS", "RBI Guidelines"],
            "data_requirements": ["customer_data", "transaction_logs"],
            "llm_output": llm_response,
            "status": "researched"
        }
        
        memory_manager.add_short(self.name, research_output)
        memory_manager.add_long("research_findings", research_output)
        
        return research_output
