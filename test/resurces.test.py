from src.ShopeeFood import ShopeeFood
import asyncio
shopee_food = ShopeeFood()

# print(shopee_food.get_locations())
# print(shopee_food.get_districts("ha Nội"))



asyncio.run(shopee_food.search(location="Hà Nội",  keyword="phở bò"))