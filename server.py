from mcp.server.fastmcp import FastMCP
from mcp.types import Resource

# Create a MCP server
mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b:int) -> int:
    """Add two numbers"""
    return a+b

@mcp.resource("greeting://{name}")
def get_weather(name: str) -> str:
    return f"Hello {name}"
