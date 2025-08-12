from mcp.server.fastmcp import FastMCP


# stateless_http=True = no per-user memory between calls.
mcp = FastMCP(name="hello-mcp",stateless_http=True)

@mcp.tool()  #register functions as callable tools.
def search_online(query: str)-> str:
    return f"Search online for {query}..."

@mcp.tool()
def get_weather(location: str)-> str:
    return f"Weather of {location} is sunny..."

# mcp.streamable_http_app() = turns the server into a web app you can run.
mcp_app = mcp.streamable_http_app() 
