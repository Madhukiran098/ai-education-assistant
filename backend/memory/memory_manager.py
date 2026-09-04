from typing import Dict, List, Any
from datetime import datetime

class MemoryManager:
    def __init__(self):
        self.short_term_memory: List[Dict] = []
        self.long_term_memory: Dict[str, Any] = {}
        self.context_window: List[Dict] = []

    def add_short(self, agent_name: str, data: Any):
        entry = {
            "agent": agent_name,
            "data": data,
            "timestamp": datetime.now().isoformat()
        }
        self.short_term_memory.append(entry)
        self.context_window.append(entry)
        if len(self.context_window) > 10:
            self.context_window.pop(0)
        print(f"[Memory] Added {agent_name} to short-term")

    def add_long(self, key: str, value: Any):
        self.long_term_memory[key] = value
        print(f"[Memory] Saved to long-term: {key}")

    def get_context(self) -> Dict:
        return {
            "recent_context": self.context_window,
            "long_term": self.long_term_memory,
            "total_interactions": len(self.short_term_memory)
        }

    def get_history(self) -> List[Dict]:
        return self.short_term_memory

    def clear_short(self):
        self.short_term_memory = []
        self.context_window = []

memory_manager = MemoryManager()
