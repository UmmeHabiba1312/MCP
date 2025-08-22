from mcp.server.fastmcp import FastMCP

mcp = FastMCP("DocumentMCP", stateless_http=True)

docs = {
    "deposition.md": "This deposition covers the testimony of Angela Smith, P.E.",
    "report.pdf": "The report details the state of a 20m condenser tower.",
    "financials.docx": "These financials outline the project's budget and expenditures.",
    "outlook.pdf": "This document presents the projected future performance of the system.",
    "plan.md": "The plan outlines the steps for the project's implementation.",
    "spec.txt": "These specifications define the technical requirements for the equipment.",
}

@mcp.tool()
def greet(name: str) -> str:
    return f"Hello, {name}!"

# TODO: Write a tool to read a doc
@mcp.tool(name="read_docs",description="Read a document by its ID")
def read_doc(doc_id: str) -> str:
    return docs[doc_id]

# TODO: Write a tool to edit a doc
@mcp.tool()
def edit_doc(doc_id: str, content: str) -> str:
    docs[doc_id] = content
    return f"Document {doc_id} has been updated."
# TODO: Write a resource to return all doc id's
# TODO: Write a resource to return the contents of a particular doc
# TODO: Write a prompt to rewrite a doc in markdown format
# TODO: Write a prompt to summarize a doc

mcp_app = mcp.streamable_http_app()