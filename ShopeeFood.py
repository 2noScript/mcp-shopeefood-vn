
from browserforge.fingerprints import Screen
import time
from camoufox.async_api import AsyncCamoufox
from constants import LOCATIONS,DOMAIN
from typing import List
from lib import load_yml,normalize_text



constrains = Screen(max_width=1920, max_height=1080)


# async with AsyncCamoufox(
#     os=["windows", "macos", "linux"],
#     screen=constrains,
#     block_images=True,
#     i_know_what_im_doing=True,
#     block_webrtc=True,
#     block_webgl=True
# ) as browser:
#     page = browser.new_page()
#     page.goto("https://shopeefood.vn/da-nang/danh-sach-dia-diem-giao-tan-noi?q=tr%C3%A0%20s%E1%BB%AFa")
#     time.sleep(60)
    


class ShopeeFood:
    def __init__(self):
        self.locations = load_yml("config/locations.yml")
        pass
    
    def get_locations(self):
        return [location["name"] for location in self.locations]
    def get_districts(self, location: str):
        for item in self.locations:
            if normalize_text(item["name"]) == normalize_text(location):
                return [district["name"] for district in item["districts"]]
        return []

    async def search(self, location: str, districts: List[str] = [], keyword: str = "", limit: int = 25):
        url = f"https://{DOMAIN}/{LOCATIONS[location]}/danh-sach-dia-diem-giao-tan-noi?q={keyword}"


    
