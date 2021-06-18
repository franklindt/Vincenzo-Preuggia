import urllib.request
import robot
#import rob

url = None

data = ""

sitemaps = []

returnCode = 0


def isDuplicate(link, urls):
    for x in range(0, len(urls)):
        if link == urls[x]:
            return True
    return False

while returnCode != 200:

    print("Enter website")

    url = input()
    if url.count("/") < 2:
        print("pls include http:// or https://")
        continue
    try:
        data = urllib.request.urlopen(url)
        returnCode = data.getcode()
        print("exited with code: " + str(returnCode))
    except Exception as err:
        print(err)

print("hi")
baseURL = url

if baseURL.count("/") > 2:
    baseURL = list(baseURL)
    chars = ["/", "/", "/", "`", "`", "`", "`", "~", "/", "/"]
    for x in range(0, 5):
        baseURL[baseURL.index(chars[x])] = chars[x+5]
    baseURL = ''.join(baseURL).split("~")[0]

pages = [url]

try:
    urllib.request.urlopen(baseURL + "/robots.txt")
    sitemaps = robot.scan(baseURL)
except:
    pass

sitemaps = sitemaps + robot.brute(baseURL)

#baseURL = baseURL[baseURL.find("/") + 2:]

data = str(urllib.request.urlopen(url).read())

def isPage(link):
    if link.count(".") > baseURL.count("."):
        return False
    return True

def crawl(web,base):
    print(web)
    data = str(urllib.request.urlopen(web).read())
    while data.find(base) >= 0:
        data = data[data.find(base):]
        if not isDuplicate(data[:data.find('"')], pages) and isPage(data[:data.find('"')]):
            pages.append(data[:data.find('"')])
        data = data[1:]
#crawl(data, baseURL)
for x in range(0, len(sitemaps)):
    crawl(sitemaps[x], baseURL)

def fin(urls, base):
    org_len = -1
    index = 0
    while org_len != len(urls):
        org_len = len(urls)
        for x in range(0, len(urls) - index):
            try:
                crawl(urls[index], base)
                index+=1
            except:
                urls.pop(index)
                x -= 1


fin(pages, baseURL)
print(pages)