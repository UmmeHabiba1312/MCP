from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="hello-mcp",stateless_http=True)

@mcp.tool()
def search_online(query: str)-> str:
    return f"Search online for {query}..."

@mcp.tool()
def get_weather(location: str)-> str:
    return f"Get weather for {location}..."

mcp_app = mcp.streamable_http_app()