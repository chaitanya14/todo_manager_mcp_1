# Todo MCP Server

## Description
A server for managing todo items using the Model Context Protocol.

## Installation
1. Clone the repository.
2. Install the dependencies using `pip install -r requirements.txt`.

## Usage
Run the server with `python -m todo_mcp_server`.

## API Endpoints
- `POST /todos` - Add a new todo item.
- `GET /todos` - List all todo items or filter by status.
- `PUT /todos/{id}` - Mark a todo item as completed.