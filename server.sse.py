from fastmcp import FastMCP

mcp = FastMCP('Demo')

@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

if __name__ == '__main__':
    mcp.run()

# run using  fastmcp run server.sse.py:mcp --transport sse --host 127.0.0.1 --port 8000

    