from src.lib.utils import load_yml,normalize_text
from typing import List

locations=load_yml("src/config/locations.yml")


def shop_locations():
    return [location["name"] for location in locations]

def shop_districts_by_location(location: str)->List[str]:
    for item in locations:
        if normalize_text(item["name"]) == normalize_text(location):
            return [district["name"] for district in item["districts"]]
    return []

def find_slug_location(location: str)->List[str]:
    for item in locations:
        if normalize_text(item["name"]) == normalize_text(location):
            return item["slug"]
    return []