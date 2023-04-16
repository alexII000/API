import requests
import json

url = 'https://api.fbi.gov/wanted/v1/list'
r = requests.get(url)

wanted_list = r.json()

filtered_list = [item for item in wanted_list['items'] if 'ViCAP Missing Persons' in item['subjects'] and item['age_max'] is not None and item['age_max'] < 25]

for item in filtered_list:
    NameCity = item['title'].title()
    weight_num = ''.join(filter(str.isdigit, item['weight']))

    print(f"Name: {NameCity}\n"
          f"FBI direct link: {item['url']}\n"
          f"Gender: {item['sex']}\n"
          f"Age: {item['age_max']}\n"
          f"Eye Color: {item['eyes']}\n"
          f"Hair Color: {item['hair']}\n"
          f"Weight: {weight_num}\n"
          f"\n")
