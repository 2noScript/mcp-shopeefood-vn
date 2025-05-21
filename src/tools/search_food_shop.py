from src.lib.worker import run_task
from src.lib.utils import view_data




async def _handle(page,url):
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
                print(e)

    page.on("response", handle_response)
    await page.goto(url,wait_until="networkidle",timeout=15000)
    return view_data(results)



async def search_food_shop(
    location: str, 
    districts: List[str] = [],
    keyword: str = "",
    limit: int = 25
    ):
    url = f"https://{DOMAIN}/{LOCATIONS[location]}/danh-sach-dia-diem-giao-tan-noi?q={keyword}"
    return await run_task(_handle, [url])
     