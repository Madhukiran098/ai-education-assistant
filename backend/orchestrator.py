from backend.agents.knowledge_agent import KnowledgeAgent
from backend.agents.research_agent import ResearchAgent
from backend.agents.technical_agent import TechnicalAgent
from backend.agents.compliance_agent import ComplianceAgent
from backend.agents.analysis_agent import AnalysisAgent
from backend.agents.decision_agent import DecisionAgent
from backend.agents.execution_agent import ExecutionAgent
from backend.memory.memory_manager import memory_manager

class Orchestrator:
    def __init__(self):
        self.agents = {
            "knowledge": KnowledgeAgent(),
            "research": ResearchAgent(),
            "technical": TechnicalAgent(),
            "compliance": ComplianceAgent(),
            "analysis": AnalysisAgent(),
            "decision": DecisionAgent(),
            "execution": ExecutionAgent()
        }
    
    def run(self, business_request: str):
        print(f"=== Starting workflow for: {business_request} ===")
        memory_manager.clear()
        
        logs = []
        
        # Sequential Execution - Enterprise Workflow
        k = self.agents["knowledge"].execute(business_request)
        logs.append({"agent": "Knowledge", "status": "done", "data": k})
        
        r = self.agents["research"].execute(business_request)
        logs.append({"agent": "Research", "status": "done", "data": r})
        
        t = self.agents["technical"].execute(business_request)
        logs.append({"agent": "Technical", "status": "done", "data": t})
        
        c = self.agents["compliance"].execute(business_request)
        logs.append({"agent": "Compliance", "status": "done", "data": c})
        
        a = self.agents["analysis"].execute(business_request)
        logs.append({"agent": "Analysis", "status": "done", "data": a})
        
        d = self.agents["decision"].execute(business_request)
        logs.append({"agent": "Decision", "status": "done", "data": d})
        
        final = self.agents["execution"].execute(business_request)
        
        return {
            "final_result": final,
            "logs": logs
        }

# Global instance
orchestrator = Orchestrator()
