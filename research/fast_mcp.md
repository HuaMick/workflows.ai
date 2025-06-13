# FastMCP Research

This document summarizes key features and concepts of the FastMCP framework, based on the official documentation ([Source](https://gofastmcp.com/llms-full.txt)).

## Overview

FastMCP is a Python framework for building Model Context Protocol (MCP) servers and clients. MCP is a standard for providing context and tools to LLMs, acting as a "USB-C port for AI". FastMCP simplifies the process by handling the protocol details, allowing developers to focus on building tools and resources.

## Core Concepts

### 1. `FastMCP` Server

The central object of an application, holding tools, resources, and prompts.

```python
from fastmcp import FastMCP

mcp = FastMCP("MyAssistantServer")
```

### 2. Tools

Tools allow LLMs to perform actions by executing Python functions. They are defined using the `@mcp.tool` decorator. FastMCP automatically generates the necessary schema from type hints and docstrings.

```python
@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```

### 3. Resources & Templates

Resources expose read-only data sources, similar to a `GET` request. They are defined with `@mcp.resource("your://uri")`. Dynamic resources can be created using placeholders in the URI.

```python
# Static resource
@mcp.resource("config://version")
def get_version():
    return "2.0.1"

# Dynamic resource template
@mcp.resource("users://{user_id}/profile")
def get_profile(user_id: int):
    # ... fetch profile
    return {"name": f"User {user_id}", "status": "active"}
```

### 4. Prompts

Prompts are reusable message templates to guide LLM interactions, defined with `@mcp.prompt`.

```python
@mcp.prompt
def summarize_request(text: str) -> str:
    """Generate a prompt asking for a summary."""
    return f"Please summarize the following text:\n\n{text}"
```

### 5. Context

The `Context` object provides access to MCP session capabilities within tools, resources, or prompts. This includes logging, making HTTP requests, reading other resources, and requesting completions from the client's LLM (`ctx.sample()`).

```python
from fastmcp import FastMCP, Context

@mcp.tool
async def process_data(uri: str, ctx: Context):
    await ctx.info(f"Processing {uri}...")
    data = await ctx.read_resource(uri)
    summary = await ctx.sample(f"Summarize: {data.content[:500]}")
    return summary.text
```

### 6. MCP Clients

The `fastmcp.Client` can be used to programmatically interact with any MCP server. It supports multiple transports.

```python
from fastmcp import Client
import asyncio

async def main():
    async with Client("my_server.py") as client:
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"Result: {result.text}")

asyncio.run(main())
```

## Running a Server

A FastMCP server can be run using the `.run()` method. It supports different transport protocols.

```python
# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    # Default transport is 'stdio'
    mcp.run()
```

## Key Features (v2.8.0)

-   **Tool Transformation**: Create enhanced variations of existing tools (e.g., rename arguments, hide parameters, add validation) without rewriting the original code.
-   **Component Control**: Use tag-based filtering to selectively enable/disable tools, resources, and prompts. Components can also be programmatically enabled or disabled.
-   **OpenAPI to Tools by Default**: A breaking change where all OpenAPI endpoints are now converted to `Tools` by default to improve compatibility with most existing MCP clients.

## Transports

FastMCP supports various transports for communication between clients and servers.

-   **Stdio**: `PythonStdioTransport`, `NodeStdioTransport`. Good for local scripts.
-   **HTTP**: `StreamableHttpTransport`. Recommended for web deployments.
-   **In-Memory**: `FastMCPTransport`. Extremely useful for testing, as it connects a client directly to a server instance in the same process.
-   **Configuration-Based**: `MCPConfigTransport` allows connecting to multiple servers defined in a configuration object.
