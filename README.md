# MCP Server Demo

A demonstration project showcasing the FastMCP framework for building and interacting with MCP (Model Control Protocol) services.

## Overview

This project demonstrates a simple MCP service implementation using FastMCP, featuring:
- A server that exposes MCP tools
- A client that can interact with the MCP service
- Server-Sent Events (SSE) support for real-time communication

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone this repository:
```bash
git clone git@github.com:sajithamma/mcpserver-demo.git
cd mcpserver-demo
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

- `server.py`: The main MCP server implementation
- `client.py`: Example client for interacting with the MCP service
- `server.sse.py`: Server implementation with SSE support
- `client.sse.py`: Client implementation with SSE support
- `requirements.txt`: Project dependencies

## Usage

### Running the Server

```bash
python server.py
fastmcp run server.py
```

### Running the Client

```bash
python client.py
```

### Using SSE Version

To use the Server-Sent Events version:

```bash
# Start the SSE server
fastmcp run server.sse.py:mcp --transport sse --host 127.0.0.1 --port 8000

# In another terminal, run the SSE client
python client.sse.py
```

## Features

- Simple MCP tool implementation (addition function)
- Asynchronous client-server communication
- Server-Sent Events support for real-time updates
- Type-safe tool definitions using Python type hints

## Dependencies

The project uses several key dependencies:
- FastMCP: The core framework for MCP services
- Starlette: ASGI framework for building web services
- Uvicorn: ASGI server implementation
- SSE-Starlette: Server-Sent Events support
- Pydantic: Data validation and settings management



