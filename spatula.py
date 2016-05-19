#!/usr/bin/python

import requests

from argparse import ArgumentParser
from lxml import html
from lxml.cssselect import CSSSelector
from requests.exceptions import MissingSchema


class Spatula:
    """ Spatula Class

    Gets a web - page from the Internet, runs a selector query on it if
    supplied, and stores the DOM element that results.
    """

    def __init__(self, url, selector=None):
        try:
            r = requests.get(url)
        except MissingSchema:
            r = requests.get('http://%s' % url)
        tree = html.fromstring(r.text)
        if selector:
            sel = CSSSelector(selector)
        else:
            sel = CSSSelector('html')
        if sel:
            self.elems = sel(tree)
        else:
            self.elems = []

    def text(self):
        return [elem.text_content() for elem in self.elems]

    def attr(self, attr):
        res = []
        for elem in self.elems:
            for k, v in elem.items():
                if k == attr:
                    res.append(v)
        return res


if __name__ == '__main__':
    parser = ArgumentParser(description='A simple web-scraper CLI.')
    parser.add_argument('url', type=str,
                        help='The URL to scrape.')
    parser.add_argument('-s', '--selector', type=str,
                        help='CSS/jQuery selector for element to find.')
    parser.add_argument('-a', '--attr', type=str,
                        help='The desired element attribute. Gets inner text if not set.')

    args = parser.parse_args()

    spatula = Spatula(args.url, args.selector)
    if not args.attr:
        for text in spatula.text():
            print text.strip()
    else:
        for attr in spatula.attr(args.attr):
            print attr.strip()
