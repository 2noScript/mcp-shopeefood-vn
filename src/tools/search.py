from src.lib.worker import run_task
from src.lib.utils import view_data
from src.lib.constant import GOTO_OPTION, DOMAIN
from src.resources import find_slug_location
from typing import List, Dict, Any

async def _extract_shop_info(item: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract relevant information from shop data.
    
    Args:
        item: Raw shop data from API
        
    Returns:
        Dict containing formatted shop information
    """
    return {
        "name": item["name"],
        "address": item["address"],
        "open_time": item["operating"].get("open_time"),
        "close_time": item["operating"].get("close_time"),
        "review": item["rating"]["total_review"],
        "rating": item["rating"]["avg"],
        "open": item["is_open"],
    }

async def _handle(page, url: str) -> str:
    """
    Handle page navigation and data extraction.
    
    Args:
        page: Browser page instance
        url: Target URL to scrape
        
    Returns:
        Formatted table of results
    """
    results = []
    
    async def handle_response(response):
        if response.url == "https://gappapi.deliverynow.vn/api/delivery/get_infos":
            try:
                data = await response.json()
                results.extend([
                    await _extract_shop_info(item) 
                    for item in data["reply"]["delivery_infos"]
                ])
            except Exception as e:
                print(f"Error processing response: {str(e)}")

    page.on("response", handle_response)
    await page.goto(url, **GOTO_OPTION)
    return view_data(results)

async def search(
    location: str, 
    districts: List[str] = [],
    keyword: str = "",
    limit: int = 25
) -> str:
    """
    Search for restaurants on ShopeeFood.
    
    Args:
        location: City name
        districts: List of district names to filter
        keyword: Search term
        limit: Maximum number of results
        
    Returns:
        Formatted table of search results
    """
    url = f"https://{DOMAIN}/{find_slug_location(location)}/danh-sach-dia-diem-giao-tan-noi?q={keyword}"
    return await run_task(_handle, [url])
     