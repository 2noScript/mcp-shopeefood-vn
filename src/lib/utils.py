import yaml
from typing import Any,List
import unicodedata
import re
import urllib
def load_yml(path: str) -> Any:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"[Error] File not found: {path}")
    except yaml.YAMLError as e:
        print(f"[Error] YAML parsing error in '{path}': {e}")
    except Exception as e:
        print(f"[Error] Unexpected error while loading '{path}': {e}")
    return None



def normalize_text(text: str) -> str:
    return re.sub(r'\s+', '_',
           unicodedata.normalize('NFD', text)
           .encode('ascii', 'ignore').decode('utf-8')
           .replace('đ', 'd').replace('Đ', 'D')
           .lower())

def view_data(data:List[Any])->str:
    return yaml.dump(data, allow_unicode=True, sort_keys=False)


def decode_url(text: str) -> str:
    return urllib.parse.unquote(text) if text else text


