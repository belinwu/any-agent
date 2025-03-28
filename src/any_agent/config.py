from enum import Enum
from pydantic import BaseModel, Field, ConfigDict


class AgentFramework(str, Enum):
    OPENAI = "openai"
    LANGCHAIN = "langchain"
    SMOLAGENTS = "smolagents"
    LLAMAINDEX = "llama_index"


class MCPTool(BaseModel):
    command: str
    args: list[str]
    tools: list[str]


class AgentConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    model_id: str
    name: str = "default-name"
    instructions: str | None = None
    api_base: str | None = None
    api_key_var: str | None = None
    tools: list[str | MCPTool] = Field(default_factory=list)
    handoff: bool = False
    agent_type: str | None = None
    model_class: str | None = None
    description: str | None = None
