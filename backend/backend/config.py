import os

class Config:
    PROJECT_NAME = "Enterprise Multi-Agent System"
    VERSION = "v0.1"
    LLM_MODEL = "gpt-4"
    MEMORY_TYPE = "hybrid"
    NUM_AGENTS = 7

    @staticmethod
    def get_env(key: str, default=None):
        return os.getenv(key, default)

config = Config()
