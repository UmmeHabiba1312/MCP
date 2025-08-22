from mcp import ClientSession,types
import asyncio
from mcp.client.streamable_http import streamablehttp_client
from contextlib import AsyncExitStack
from pydantic import AnyUrl
import json

class MCPClient:
    def __init__(self,url):
        self.url = url
        self.stack = AsyncExitStack()
        self._sess = None
    # async def list_tools(self):
    #     async with self.session as session:
    #         response = (await session.list_tools()).tools
    #         return response
    async def __aenter__(self):
        read , write , _ = await self.stack.enter_async_context(
            streamablehttp_client(self.url)
        )

        self._sess = await self.stack.enter_async_context(
            ClientSession(read, write)
        )

        await self._sess.initialize()
        return self
    async def __aexit__(self, exc_type, exc_val, exc_tb):
         await self.stack.aclose()

    async def list_tools(self)->list[types.Tool]:
        assert self._sess, "Session is not available"
        response = (await self._sess.list_tools()).tools
        return response

    async def call_tool(self, tool_name, *args, **kwargs):
        assert self._sess, "Session is not available"
        response = await self._sess.call_tool(tool_name, *args, **kwargs)
        return response

    async def list_resources(self)->list[types.Resource]:
        assert self._sess, "Session is not available"
        response: types.ListResourcesResult = await self._sess.list_resources()
        return response.resources

    async def list_resource_templates(self) -> list[types.ResourceTemplate]:
        assert self._sess, "Session is not available"
        response: types.ListResourceTemplatesResult = await self._sess.list_resource_templates()
        # print("Resource templates:", response.__dict__)
        return response.resourceTemplates
    
    async def read_resources(self, uri:str) -> types.ReadResourceResult:
        assert self._sess, "Session is not available"
        # _url = AnyUrl(uri)
        response = await self._sess.read_resource(AnyUrl(uri))
        # print("Read resource response:", response.__dict__)
        resources = response.contents[0]
        if isinstance(resources, types.TextResourceContents):
            if resources.mimeType == "application/json":
                try:
                    return json.loads(resources.text)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
        return resources.text

async def main():
    async with MCPClient("http://localhost:8000/mcp") as client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}\n")
        for tool in tools:
            print(f"Tool: {tool}\n")

        # call server greet tool
        response = await client.call_tool("greet", {"name": "habiba"})
        print(f"Greet tool response: {response}\n")

        resources = await client.list_resources()
        print(f"Available Resources: {resources}\n")

        read_resources = await client.read_resources("docs://documents")
        print(f"Read Resources response: {read_resources}\n")

        resource_templates = await client.list_resource_templates()
        # print(f"Resource Templates: {resource_templates[0].uriTemplate}\n")
        intro_uri = resource_templates[0].uriTemplate.replace("{doc_name}", "intro")
        data = await client.read_resources(intro_uri)
        print(f"Intro Document Data: {data}\n")

        # for t in resource_templates:
        #     print(f"Template URI: {t.uriTemplate}\n")


asyncio.run(main())


# TODO
# Create tool on mcp server and  call it on client
# and baqi sari recources and send png etc bhi rakhna hey \
# from mcp import ClientSession,types  mein se types  ko bhi explore krna hey
# use binary scheme like binary://logo  > audio  / pdf / images