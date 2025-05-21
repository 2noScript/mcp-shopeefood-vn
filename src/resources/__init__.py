from src.lib.constant import LOCATIONS,DOMAIN
from src.lib.utils import load_yml,normalize_text




locations=load_yml("src/config/locations.yml")


def get_locations():
    return [location["name"] for location in locations]

def get_districts(location: str):
    for item in self.locations:
        if normalize_text(item["name"]) == normalize_text(location):
            return [district["name"] for district in item["districts"]]
    return []
