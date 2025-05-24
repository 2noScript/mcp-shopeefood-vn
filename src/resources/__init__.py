from src.lib.utils import load_yml,normalize_text,view_data,decode_url
from typing import List


locations=load_yml("src/config/shop_locations.yml")


def shop_cities()->str:
    return view_data([item["name"] for item in locations])

def shop_city_districts(city_name:str)->str:
    for item in locations:
        if normalize_text(item["name"]) == normalize_text(decode_url(city_name)):
            return view_data([district["name"] for district in item["districts"]])
    return ""



def find_slug_by_city_name(city_name: str)->List[str]:
    for item in locations:
        if normalize_text(item["name"]) == normalize_text(city_name):
            return item["slug"]
    return []
