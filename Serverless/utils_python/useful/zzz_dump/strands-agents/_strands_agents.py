# https://www.youtube.com/watch?v=TD2ihEBkdkY
# pip install -U strands-agents strands-agents-tools

import os
# cpu_count = os.cpu_count
# os.environ["AWS_DEFAULT_REGION"] = "eu-west-2" 
# os.environ["AWS_ACCESS_KEY_ID"]=""
# os.environ["AWS_SECRET_ACCESS_KEY"]=""
# os.environ["AWS_SESSION_TOKEN"]=""

# from strands.agent import Agent, AgentResult, ConversationManager, NullConversationManager, SlidingWindowConversationManager, SummarizingConversationManager
# from strands.event_loop import event_loop, error_handler, message_processor, streaming
# from strands.handlers import callback_handler, tool_handler, PrintingCallbackHandler, CompositeCallbackHandler
# from strands.types import models, tools, exceptions, traces, event_loop, streaming, media, content
# from strands.multiagent import a2a

from strands import Agent 
from strands_tools import calculator, current_time
# agent_graph, batch, cron, calculator, current_time, editor, environment, file_read, file_write, generate_image, http_request, image_reader, journal, 
# load_tool, mem0_memory, memory, nova_reels, python_repl, retrieve, shell, slack, sleep, speak, stop, swarm, think, use_aws, use_llm, workflow

# from strands.models.anthropic, openai, bedrock, litellm, llamaapi, ollama, BedrockModel
# pip install 'strands-agents[ollama]'
# from strands.models.ollama import OllamaModel
# my_model  = OllamaModel(host="http://localhost:11434", model_id="llama3.2:latest", max_tokens=1024, temperature=1.0, top_p=None, keep_alive=False)

# pip install 'strands-agents[anthropic]'
# from strands.models.anthropic import AnthropicModel
# my_model = AnthropicModel(client_args={"api_key: key"}, model_id="claude-3-7-sonnet-20250219", max_tokens=1028)

# pip install 'strands-agents[bedrock]'
# from strands.models.bedrock import BedrockModel
# my_model = BedrockModel(boto_session=session, boto_client_config=botoconfig, region_name="us-east-1", \
#                         model_id="us.anthropic.claude-3-5-sonnet-202406020-v1:0", max_tokens=1024, temperature=1.0, top_p=None, streaming=True)

# agent = Agent(model="", messages=Messages, tools=[], system_prompt="", name="AgentName", description="AgentDescription",  callback_handler=None, 
#               conversation_manager=None, max_parallel_tools=1, load_tools_from_directory=False, record_direct_tool_call=False, trace_attributes=False)

# Defaults to Claude 3.7
agent = Agent(tools=[calculator, current_time]) # callback_handler= PrintingCallbackHandler)
# agent = Agent(model=my_model, tools=[calculator, current_time])

prompt = "I was born on May 22, 1985. What is my age in days today?"

kwargs = {}
response = agent(prompt, **kwargs)
print(response)


