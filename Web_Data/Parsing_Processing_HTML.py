from html.parser import HTMLParser

meta_count = 0

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print("Encountered comment: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_starttag(self, tag, attrs):
        global meta_count
        if tag == 'meta':
            meta_count += 1
        print("Encountered tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

        if attrs.__len__() > 0:
            print("\tAttributes:")
            for a in attrs:
                print("\t", a[0], "=", a[1])

    def handle_endtag(self, tag):
        print("Encountered tag: ", tag)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])

    def handle_data(self, data):
        if data.isspace():
            return
        print("Encountered comment: ", data)
        pos = self.getpos()
        print("\tAt line: ", pos[0], " position ", pos[1])


def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    f = open("samplehtml.html")
    if f.mode == 'r':
        contents = f.read()
        parser.feed(contents)

    print("Met tags found: " + str(meta_count))


if __name__ == '__main__':
    main()
