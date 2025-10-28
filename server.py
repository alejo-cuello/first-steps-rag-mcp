from mcp.server.fastmcp import FastMCP

# Create a MCP server
mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b:int) -> int:
    """Add two numbers"""
    return a+b