import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

outfile = open('hn.json','w')

json.dump(r.json(), outfile, indent=4)

submissionIDsList = r.json()


url = 'https://hacker-news.firebaseio.com/v0/item/35457341.json'
r = requests.get(url)
outfile = open('hn2.json','w')
response_dict = r.json()
json.dump(response_dict, outfile, indent=4)

# Explore the structure of the data.
list_of_dicts = response_dict['kids']
for id in submissionIDsList[:21]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{id}.json'
    r = requests.get(url)
    response_dict = r.json()
    submissions_list = []

    title = response_dict['title']
    link =f'https://news.ycomvinator.com/item?id={id}'

    print(f"Title: {response_dict['title']}")
    print(f"Link: http://new.ycombinator.com/item?id={id}")
    try:
        comments = response_dict['descendants']
    except:
        comments = 0 

    a_dict = {'title': title, 'link':link, 'comments':comments}

    submissions_list.append(a_dict)

from operator import itemgetter

submissions_list = sorted(submissions_list, key=itemgetter('comments'), reverse=True)

for x in submissions_list:
    print(f"Title: {x['title']}")
    print(f"Link: {x['link']}")
    print(f"Comments: {x['comments']}")

    