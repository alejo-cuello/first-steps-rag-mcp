# from azure.ai.inference import ChatCompletionsClient
# from azure.ai.inference.models import SystemMessage, UserMessage
# from azure.core.credentials import AzureKeyCredential
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import os

server_params = StdioServerParameters(
    command="mcp",
    args=["run","server.py"],
    env=None
)

# def call_llm(prompt, functions):
#     token = os.getenv("token") 
#     endpoint = ""
#     model_name = ""
    
#     client = ChatCompletionsClient(
#         endpoint=endpoint,
#         credential=AzureKeyCredential(token)
#     )
    
#     response = client.complete(
#         messages=[
#             {
#             "role": "system",
#             "content": "You are a helpful assistant.",
#             },
#             {
#             "role": "user",
#             "content": prompt,
#             },
#         ],
#         model=model_name,
#         tools = functions,
#         temperature=1.,
#         max_tokens=150,
#         top_p=1.    
#     )

#     response_message = response.choices[0].message
    
#     functions_to_call = []
    
#     if response.messagetool_calls:
#         for tool_call in response_message.tool_calls:
#             print("TOOL: ", tool_call)
#             name = tool_call.function.name
#             args = json.loads(tool_call.function.arguments)
#             functions_to_call.append({ "name": name, "args": args })

#     return functions_to_call

# def convert_to_llm_tool(tool):
#     tool_schema = {
#         "type": "function",
#         "function": {
#             "name": tool.name,
#             "description": tool.description,
#             "type": "function",
#             "parameters": {
#                 "type": "object",
#                 "properties": tool.inputSchema["properties"]
#             }
#         }
#     }

#     return tool_schema

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read,write) as session:
            await session.initialize()
                
            tools = await session.list_tools()
            for t in tools:
                print(f"Resource {t}")
                
            # content, mimetype = await session.read_resource("greeting://hello")
            # print(content, mimetype)
            
            # result = await session.read_tool("add", arguments={"a":1, "b":7})
            # print(result.content)
            
            # functions = []
            
            # prompt = "Add 2 to 20"

            # functions_to_call = call_llm(prompt, functions)

            # for f in functions_to_call:
            #     result = await session.call_tool(f["name"], arguments=f["args"])
            #     print("TOOLS result: ", result.content)
                
if __name__ == "__main__":
    import asyncio

    asyncio.run(run())