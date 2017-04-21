from HTMLParser import HTMLParser
 
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
 
    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "href" or variable == "src":
                        self.links.append(value)
 
if __name__ == "__main__":
    html_code = """
    <a href="www.google.com"> google.com</a>
    <A Href="www.pythonclub.org"> PythonClub </a>
    <A HREF = "www.sina.com.cn"> Sina </a>
    <A src = "www.sohu.com.cn"> Sohu </a>
    """
    hp = MyHTMLParser()
    hp.feed(html_code)
    print hp.getpos()
    print hp.get_starttag_text()
    hp.close()
    print(hp.links)
