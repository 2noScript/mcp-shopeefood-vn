
from browserforge.fingerprints import Screen
import time
from camoufox.async_api import AsyncCamoufox
from constants import LOCATIONS,DOMAIN



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
    
async def search(location:str,districts:str,keyword:str):
    url=f"https://{DOMAIN}/{LOCATIONS[location]}/danh-sach-dia-diem-giao-tan-noi?q={keyword}"
    pass

def get_location():
    return list(LOCATIONS.keys())


    
