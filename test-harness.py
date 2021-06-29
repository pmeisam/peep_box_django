from urllib.request import urlopen, Request
import urllib


print("*********************** TEST HARNESS ***********************")


url = "https://iranproud2.net/index.html?x05prwTuyxnoEflAJSyK"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
try:
    req = Request(url=url, headers=headers)
    page = urlopen(req)
except urllib.HTTPError as e:
    print(e)


html_bytes = page.read()
html = html_bytes.decode("utf-8")


img = html.find("<img")

print(img)
