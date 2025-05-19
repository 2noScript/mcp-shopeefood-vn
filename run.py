from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount, Host
from ShopeeFood import ShopeeFood
from typing import List
import urllib.parse

shopee_food = ShopeeFood()


mcp = FastMCP(
    name="mcp-server",

    
)


@mcp.resource("resource://locations")
def get_locations() -> List[str]:
    return shopee_food.get_locations()

@mcp.resource("resource://districts/{location}")
def get_districts(location: str) ->  List[str]:
    return shopee_food.get_districts(urllib.parse.unquote(location))


@mcp.tool()
def searchFoodShop(location: str, districts: List[str] = [], keyword: str = "", limit: int = 25) ->  List[any]:
    return [location, districts, keyword, limit]

if __name__ == "__main__":
    mcp.run(transport="sse") 