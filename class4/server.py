# CLASS 5
from mcp.server.fastmcp import FastMCP
# from mcp.shared.exceptions import Resource 
mcp = FastMCP(name="MCP Server", stateless_http=True)

docs = {
    "intro":"Welcome to the MCP Server!",
    "readme": "This is the readme for the MCP Server.",
    "guide": "Refer to the documentation for details."
}

# URI
# scheme://host/endpoint
# http://panaversity/courses or http://localhost:8000/courses
@mcp.resource("docs://documents",
              name="Documentation",
              description="List of available documentation",
              title="Documentation",
              mime_type="application/json"
              )
def list_docs():
    "list all available documentation"
    return list(docs.keys())


# print("list_docs: ", list_docs())

@mcp.resource("docs://documents/{doc_name}",
              mime_type="application/json"
              )
def read_doc(doc_name: str):
    "get a specific document"
    # First method 
    # if doc_name in docs:
    #     return {"name": doc_name, "content": docs[doc_name]}
    # else:
    #     return mcp.ResourceNotFoundError(f"Document {doc_name} not found")
    
    # OR same second method
    return docs.get(doc_name, f"Document {doc_name} not found")


mcp_server = mcp.streamable_http_app()