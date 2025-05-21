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

### Prerequisites

- Docker and Docker Compose
- Git

### Using Docker Compose

```bash
git clone https://github.com/2noScript/mcp-shopeefood-vn.git
cd mcp-shopeefood-vn

docker-compose up -d --build
```

```json
{
  "mcpServers": {
    "mcp-test": {
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
- `location`: Location (e.g. `Hà Nội`)
- `districts`: Districts (e.g.  ["Hoàn Kiếm", "Ba Đình"])
- `keyword`: Keyword (e.g. `Bún chả`)
- `limit`: Limit (e.g. `25`)

<h2 id="tools">Demo</h2>



https://github.com/user-attachments/assets/0b4fffce-f86b-4ee3-a696-6383dfcf5051



