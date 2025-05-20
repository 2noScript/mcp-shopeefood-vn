
from camoufox.async_api import AsyncCamoufox
from browserforge.fingerprints import Screen
from typing import List
from src.lib import load_yml,normalize_text
from src.constants import LOCATIONS,DOMAIN
import time
import yaml





constrains = Screen(max_width=1280, max_height=720)


class ShopeeFood:
    def __init__(self):
        self.locations = load_yml("src/config/locations.yml")

    async def __run_task(self, handle, args):
        try:
            async with AsyncCamoufox(
              i_know_what_im_doing=True,
              screen=constrains,
              os=('windows','macos', 'linux'),
              block_images=True,
              humanize=True,
              headless=True,
              block_webrtc=True
            ) as browser:
                 page = await browser.new_page()
                 result = await handle(page, *args)
                 print(result)
                 return result
        except Exception as e:
             print(e)
             raise

    
    def get_locations(self):
        return [location["name"] for location in self.locations]

    def get_districts(self, location: str):
        for item in self.locations:
            if normalize_text(item["name"]) == normalize_text(location):
                return [district["name"] for district in item["districts"]]
        return []



    async def search(self, 
            location: str, 
            districts: List[str] = [], 
            keyword: str = "", 
            limit: int = 25):
        url = f"https://{DOMAIN}/{LOCATIONS[location]}/danh-sach-dia-diem-giao-tan-noi?q={keyword}"
        
        return await self.__run_task(self.__handle_search, [url])

    
    async def __handle_search(self, page,url):

        results=[]
        async def handle_response(response):
            if response.url == "https://gappapi.deliverynow.vn/api/delivery/get_infos":
                try:
                    data = await response.json()
                    for item in data["reply"]["delivery_infos"]:
                        results.append(
                            {
                                "name": item["name"],
                                "address": item["address"],
                                "open_time":item["operating"].get("open_time"),
                                "close_time":item["operating"].get("close_time"),
                                "review": item["rating"]["total_review"],
                                "rating": item["rating"]["avg"],
                                "open": item["is_open"],
                            }
                        )

                except Exception as e:
                    print("⚠️ Không thể parse JSON:", e)

        page.on("response", handle_response)
        await page.goto(url,wait_until="networkidle",timeout=15000)


        # time.sleep(10)
        # print(tabulate(results, headers="keys", tablefmt="grid",showindex=True))
        # return tabulate(results, headers="keys", tablefmt="github",showindex=True)
        return yaml.dump(results, allow_unicode=True,sort_keys=False)



    
