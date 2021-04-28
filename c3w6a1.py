import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter url: ")
html = urllib.request.urlopen(url)
data = html.read().decode()

js = json.loads(data)

total = 0
for i in range(len(js["comments"])):
    total = total + js["comments"][i]["count"]


print (total)