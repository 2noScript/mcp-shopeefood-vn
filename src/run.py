from mcp.server.fastmcp import FastMCP
from typing import List,Any
from src.resources import shop_cities,shop_city_districts
from src.tools.search import search
from src.lib.hint import ResourcesHint,ToolsHint

mcp = FastMCP(
    name="mcp-shopeefood-vn",
    host="0.0.0.0"
)



@mcp.resource(
    uri="cities://all",
    name="cites",
    description=ResourcesHint.CITIES)
def get_cities() -> str:
    return shop_cities()

@mcp.resource(
    uri="cities://districts/{city_name}",
    name="districts",
    description=ResourcesHint.DISTRICTS
    )
def get_city_districts(city_name:str) -> str:
    return shop_city_districts(city_name)



@mcp.tool(
   description=ToolsHint.SEARCH_FOOD_SHOP
)
async def search_food_shop(
    city: str, 
    districts: List[str] = [], 
    keyword: str = "", 
    limit: int = 25) -> str:

    return await search(
        city=city,
        districts=districts,
        keyword=keyword,
        limit=limit
    )


if __name__ == "__main__":
    mcp.run(transport="sse")