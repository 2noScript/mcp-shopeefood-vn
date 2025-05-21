from mcp.server.fastmcp import FastMCP
from typing import List
from src.resources import get_locations,get_districts
import urllib.parse

mcp = FastMCP(
    name="mcp-shopeefood-vn",
    port=4003
)

@mcp.resource("resource://locations")
def get_locations() -> List[str]:
    return get_locations()

@mcp.resource("resource://districts/{location}")
def get_districts(location: str) ->  List[str]:
    return get_districts(urllib.parse.unquote(location))


# @mcp.tool()
# async def  search_food_shop(
#     location: str, 
#     districts: List[str] = [], 
#     keyword: str = "", 
#     limit: int = 25) ->  str:
#     return await shopee_food.search(
#         location=urllib.parse.unquote(location),
#         districts=[urllib.parse.unquote(district) for district in districts],
#         keyword=urllib.parse.unquote(keyword),
#         limit=limit
#     )

if __name__ == "__main__":
    mcp.run(transport="sse") 