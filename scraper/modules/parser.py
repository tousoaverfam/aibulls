from bs4 import BeautifulSoup

def parse(html):

    return BeautifulSoup(
        html,
        "html.parser"
    )
