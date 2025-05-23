from src.tools.search import search
import asyncio

asyncio.run(search_food_shop(
    location="hồ chí minh",
    districts=["quận 1"],
    keyword="bún",
))