# ShopeeFood MCP Server

<img src="https://github.com/2noScript/mcp-shopeefood-vn/blob/main/docs/img/shopeefoodvn.png?raw=true" >

## Overview

MCP Server for interacting with ShopeeFood Vietnam, providing tools to search and retrieve restaurant information.

## Features

- Search restaurants by location and keywords
- Get list of supported cities and districts
- Filter results by multiple criteria
- Real-time data from ShopeeFood
- Automated browser management
- Resource-efficient operation

## Installation

```bash
git clone https://github.com/2noScript/mcp-shopeefood-vn.git
cd mcp-shopeefood-vn
```

- `Normal`

```bash
  uv pip install -r requirements.txt 
  uv run -m camoufox fetch
  uv run -m src.run
```

- `Docker Compose`

```bash
docker-compose up -d --build
```
- Configure the MCP server to use SSE as the transport protocol.
```json
{
  "mcpServers": {
    "mcp-shopeefood-vn": {
      "url": "http://localhost:8000/sse",
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

<h2 id="tools">Tools</h2>

### `search_food_shop`

List all information related to the specified keyword.
**Arguments:**

- `city`: city name  (e.g. `Hà Nội`)
- `districts`: Districts (e.g. ["Hoàn Kiếm", "Ba Đình"])
- `keyword`: Keyword (e.g. `Bún chả`)
- `limit`: Limit (e.g. `25`)

<h2 id="tools">Demo with CLINE</h2>

https://github.com/user-attachments/assets/0b4fffce-f86b-4ee3-a696-6383dfcf5051


<h2 id="tools">Demo with n8n gemini agent</h2>

<img src="https://github.com/2noScript/mcp-shopeefood-vn/blob/main/docs/img/n8n_gemini_agent.png?raw=true" >
