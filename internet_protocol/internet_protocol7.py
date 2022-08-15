import urllib.request


def get_wikidocks(page):
    print("wikidocs page:{}".format(page))  # page 호출 시 출력
    resource = "https://wikidocs.net/{}".format(page)
    with urllib.request.urlopen(resource) as s:
        with open("wikidocs_%s.html" % page, "wb") as f:
            f.write(s.read())
