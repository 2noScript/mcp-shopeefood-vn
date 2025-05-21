from src.tools.search import search_food_shop
import asyncio
asyncio.run(search_food_shop(
    location="hồ chí minh",
    districts=["quận 1"],
    keyword="bún",
))