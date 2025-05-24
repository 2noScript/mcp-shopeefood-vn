from src.tools.search import search
import asyncio

asyncio.run(search(
    location="hồ chí minh",
    districts=["quận 1"],
    keyword="bún",
))