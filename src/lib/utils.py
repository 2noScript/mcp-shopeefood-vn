import yaml
from typing import Any,List
import unicodedata
import re

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
    text = unicodedata.normalize('NFD', text)                         
    text = re.sub(r'[\u0300-\u036f]', '', text)                        
    text = text.replace('đ', 'd').replace('Đ', 'D')                   
    text = text.lower()                                              
    text = re.sub(r'\s+', '_', text)                                  
    return text

def view_data(data: List[dict]):
    return yaml.dump(data, allow_unicode=True, sort_keys=False)
