import urllib.request


def main():
    web_url = urllib.request.urlopen("http://www.google.com")
    # print status request code
    print("result code: " + str(web_url.getcode()))

    # get web url data
    data = web_url.read()
    print(data)


if __name__ == '__main__':
    main()
