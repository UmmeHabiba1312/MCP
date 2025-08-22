from mcp.server.fastmcp import FastMCP

mcp_app = FastMCP(name="MCP Client",stateless_http=True)

@mcp_app.tool()
def greet(name:str)->str:
    return f"Hello, {name}!!"


mcp_server = mcp_app.streamable_http_app()


