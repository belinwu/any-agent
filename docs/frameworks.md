# Agent Frameworks

Here you can find the frameworks currently supported in `any-agent`, along with some basic examples.

!!! info

    If you are missing any agent framework, check the [existing issues](https://github.com/mozilla-ai/any-agent/issues?q=is%3Aissue%20state%3Aopen%20label%3Aframeworks)
    to see if it has been already requested and comment/upvote on that issue.

    If there is no existing issue, don't hesitate to request and/or contribute it.

## Examples

=== "Google ADK"

    [Google ADK Repo](https://github.com/google/adk-python)

    ```python
    from any_agent import AnyAgent, AgentConfig
    agent = AnyAgent.create(
        "google",
        AgentConfig(
            model_id="gpt-4o-mini"
        )
    )
    agent.run("Which Agent Framework is the best??")
    ```

=== "🦜🔗 LangChain"

    [LangChain Repo](https://github.com/langchain-ai/langchain)

    ```python
    agent = AnyAgent.create(
        "langchain",
        AgentConfig(
            model_id="gpt-4o-mini"
        )
    )
    agent.run("Which Agent Framework is the best??")
    ```

=== "🗂️ LlamaIndex 🦙"

    [LLamaIndex Repo](https://github.com/run-llama/llama_index)

    ```python
    agent = AnyAgent.create(
        "llama_index",
        AgentConfig(
            model_id="gpt-4o-mini"
        )
    )
    agent.run("Which Agent Framework is the best??")
    ```

=== "OpenAI Agents SDK"

    [OpenAI Agents Repo](https://github.com/openai/openai-agents-python)

    ```python
    agent = AnyAgent.create(
        "openai",
        AgentConfig(
            model_id="gpt-4o-mini"
        )
    )
    agent.run("Which Agent Framework is the best??")
    ```

=== "🤗 smolagents"

    [smolagents Repo](https://github.com/huggingface/smolagents)

    ```python
    agent = AnyAgent.create(
        "smolagents",
        AgentConfig(
            model_id="gpt-4o-mini"
        )
    )
    agent.run("Which Agent Framework is the best??")
    ```

=== "Agno Agents"
    [Agno Agents Repo](https://github.com/agno-agi/agno)

    ```python
    agent = AnyAgent.create(
        "agno",
        AgentConfig(
            model_id="gpt-4o-mini"
        )
    )
    agent.run("Which Agent Framework is the best??")
    ```

## Models

The model used by an agent is defined by 3 arguments `model_id`, `model_type` and `model_args`.

A common usage of `model_args` is to specify a custom `api_base` and/or `api_key`:

```python
from any_agent import AnyAgent, AgentFramework, AgentConfig
agent = AnyAgent.create(
    "smolagents",
    AgentConfig(
        model_id="llama3.2",
        model_args={
            "api_base": "http://localhost:11434/v1"
        }
    )
)
agent.run("Which Agent Framework is the best??")
```

If you just specify `model_id` (as in the examples above), the agent will use the default `model_type` that we have selected
for that framework and no `model_args`.


!!! tip

    For frameworks that have support for [`LiteLLM`](https://github.com/BerriAI/litellm) (`google`, `langchain`, `llama_index`, `smolagents`)
    we use it as default `model_type`, allowing you to use the same `model_id` syntax across these frameworks.
