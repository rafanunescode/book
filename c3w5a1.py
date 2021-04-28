import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input("Enter url: ")
html = urllib.request.urlopen(url).read()
data = ET.fromstring(html)
total = 0

for tag in data.findall("comments/comment"):
    total = total + int(tag.find(".//count").text)

print (total)