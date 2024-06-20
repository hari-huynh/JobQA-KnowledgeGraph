from tools import kg_search
from tools.kg_search import lookup_kg
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from utils.utils import init_

tools = [lookup_kg]

with open("prompts/react_prompt.txt", "r") as file:
    react_template = file.read()


react_prompt = PromptTemplate(
    input_variables = ["tools", "tool_names", "input", "agent_scratchpad"],
    template = react_template
)


_, llm = init_()

# Init ReAct agent
agent = create_react_agent(llm, tools, react_prompt)
agent_executor = AgentExecutor(
    agent = agent,
    tools = tools,
    verbose = True
)

if __name__ == "__main__":
    # Test ReAct Agent
    question = {
        "input": "Have any company recruit Machine Learning jobs?"
    }
    result = agent_executor.invoke(question)
    print(result)




