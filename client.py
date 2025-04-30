from fastmcp import Client
import asyncio
async def main():
    async with Client("/Users/sajithmr/coding/mcpdays/server.py") as client:
        # Call a tool
        tools = await client.list_tools()
        print(tools)

        result = await client.call_tool("add", {"a": 10, "b": 2})
        print(result)


if __name__ == "__main__":
    asyncio.run(main())

