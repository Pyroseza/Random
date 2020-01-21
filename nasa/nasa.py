import requests, os
from bs4 import BeautifulSoup
import json
import webbrowser
print("Input date (YYYY-MM-DD): ")
date = str(input())

conf_path = 'config.json'
with open(conf_path) as conf_file:
    config = json.load(conf_file)
key = config['nasa_api_key']

urlencode = f"https://api.nasa.gov/planetary/apod?api_key={key}" + "&date=%s" % date
url = requests.get(urlencode)
parse = BeautifulSoup(url.content, "html.parser")
data = parse.findAll(text=True)
d = json.loads(str(parse))
print(d)
if 'copyright' in d:
    print(d['copyright'],'\n', d['date'],'\n',d['explanation'])
    if 'hdurl' in d:
        webbrowser.open(str(d['hdurl']))
    else:
        webbrowser.open(str(d['url']))
else:
    print(d['date'],'\n',d['explanation'] )
    if 'hdurl' in d:
        webbrowser.open(str(d['hdurl']))
    else:
        webbrowser.open(str(d['url']))
