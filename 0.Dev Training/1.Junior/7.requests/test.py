import requests

r = requests.get('http://github.com/timeline.json')

print r.content
