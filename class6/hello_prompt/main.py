from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
mcp = FastMCP(stateless_http=True,name="Hello prompt")

@mcp.prompt(name="greet",description="This is also about hello_prompt",title="Hello Prompt")
def hello_prompt(name:str)->list[base.UserMessage]:
    user_msg = f"Hello {name}"
    return [base.UserMessage(content=user_msg),base.AssistantMessage(content="Hello, its nice to meet you!")]

mcp_server = mcp.streamable_http_app()