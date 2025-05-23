from mcp.server.fastmcp import FastMCP
from typing import List
from src.resources import shop_locations,shop_districts_by_location
from src.tools.search import search
from src.lib.hint import ResourcesHint,ToolsHint
from src.lib.utils import decode_url

mcp = FastMCP(
    name="mcp-shopeefood-vn",
    host="0.0.0.0"
)

@mcp.resource(
    uri="locations://main",
    description=ResourcesHint.LOCATIONS)
def get_locations() -> List[str]:
    return shop_locations()

@mcp.resource(
    uri="districts://{location}",
    description=ResourcesHint.DISTRICTS)
def get_districts(location: str) -> List[str]:
    return shop_districts_by_location(decode_url(location))

@mcp.tool(
   description=ToolsHint.SEARCH_FOOD_SHOP
)
async def search_food_shop(
    location: str, 
    districts: List[str] = [], 
    keyword: str = "", 
    limit: int = 25) -> str:

    return await search(
        location=decode_url(location),
        districts=[decode_url(district) for district in districts],
        keyword=decode_url(keyword),
        limit=limit
    )

if __name__ == "__main__":
    mcp.run(transport="sse")