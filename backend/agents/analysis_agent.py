from backend.llm.client import llm_client
from backend.memory.memory_manager import memory_manager

class AnalysisAgent:
    def __init__(self):
        self.name = "AnalysisAgent"
        self.role = "Senior Data Analyst - Risk & Strategy"

    def execute(self, business_request: str) -> dict:
        print(f"[{self.name}] Analyzing: {business_request}")
        
        context = memory_manager.get_context()
        research = context.get('long_term', {}).get('research_findings', {})
        
        prompt = f"""
        Business Request: {business_request}
        Research Data: {research}
        
        Task: Perform deep analysis.
        Include: 1. SWOT analysis 2. Risk matrix 3. Cost-benefit 4. KPIs
        Provide quantifiable insights.
        """
        
        llm_response = llm_client.generate(prompt, self.name)
        
        analysis_output = {
            "role": self.role,
            "swot": {"strengths": 3, "weaknesses": 2, "opportunities": 4, "threats": 2},
            "risk_score": "Medium-High",
            "roi_estimate": "180% in 12 months",
            "kpis": ["customer_retention", "fraud_reduction", "compliance_score"],
            "llm_output": llm_response,
            "status": "analyzed"
        }
        
        memory_manager.add_short(self.name, analysis_output)
        memory_manager.add_long("analysis_report", analysis_output)
        
        return analysis_output
