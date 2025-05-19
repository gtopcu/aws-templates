
import asyncio

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# export OPENAI_API_KEY=xxxxxxxxxxxxxxxxxx

model = ChatOpenAI(model="gpt-4o")
server_parameters = StdioServerParameters(
    command="python",
    args=["mcp_server.py"]
)

# def my_func(*, input:str, val:int): ...
# my_func("sth", 0)

async def main():
    async with stdio_client(server_parameters) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)

            agent = create_react_agent(model, tools)
            response = await agent.ainvoke({"messages":"Analyze how revenue of MSFT changes over time"})
            print(response)

if __name__ == "__main__":
    asyncio.run(main())