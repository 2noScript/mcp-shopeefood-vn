# ShopeeFood MCP Server

<img src="https://github.com/2noScript/mcp-shopeefood-vn/blob/main/docs/img/shopeefoodvn.png?raw=true" width="128">


<h2 id="tools">Features</h2>
<h2 id="tools">Setting</h2>

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

