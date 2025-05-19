import json

# Mở và đọc file JSON
with open('cities.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


results=[]
for item in data:
    districts=[]
    for  dis in item['districts']:
        districts.append({
                "name": dis["name"],
                "district_id": dis["district_id"],
                "url_rewrite_name": dis["url_rewrite_name"],
        })
    item['districts']=districts
    results.append(item)
print(results)


with open('output.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, ensure_ascii=False, indent=4)
