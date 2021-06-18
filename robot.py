import urllib.request

pos_sitemaps = [
    "/sitemap.xml",
    "/sitemap_index.xml",
    "/sitemap-index.xml",
    "/sitemap/",
    "/post-sitemap.xml",
    "/sitemap/sitemap.xml",
    "/sitemap/index.xml",
    "/rss/",
    "/rss.xml",
    "/sitemapindex.xml",
    "/sitemap.xml.gz",
    "/sitemap_index.xml.gz",
    "/sitemap.php",
    "/sitemap.txt",
    "/atom.xml"
]


def isDuplicate(link, urls):
    for x in range(0, len(urls)):
        if link == urls[x]:
            return True
    return False

def filter(urls):
    org_len = 0
    while org_len != len(urls):
        org_len = len(urls)
        for x in range(0, len(urls)):
            data = str(urllib.request.urlopen(urls[x]).read())
            while data.find("http") >= 0:
#                if x == 6:
#                    print(len(data))
#                if x == 6:
#                    print(data)
#                    return
                data = data[data.find("http"):]
                if data[:data.find('"')].find(".xml") >= 0 and not isDuplicate(data[:data.find('.xml') + 4], urls):
                    try:
                        urllib.request.urlopen(data[:data.find('.xml') + 4])
                        urls.append(data[:data.find('.xml')+4])
                    except Exception as err:
                        print(err)
                        pass
                data = data[1:]
def scan(url):

    results = []

    data = str(urllib.request.urlopen(url + "/robots.txt").read())
    while data.find("Sitemap") >= 0:
        data = data[data.find("Sitemap") + 7:]
        results.append(data[data.find("http"):data.find(".xml") + 4])
    filter(results)
    return results

def brute(link):
    sitemaps = []
    for x in range(0, len(pos_sitemaps)):
        try:
            urllib.request.urlopen(link + pos_sitemaps[x])
            sitemaps.append(link + pos_sitemaps[x])
        except:
            pass
    filter(sitemaps)
    return sitemaps


#scan("https://bbc.com" + "/robots.txt")