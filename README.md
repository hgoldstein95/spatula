# Spatula

  A simple command line interface for scraping web-pages.


## Why do I need it?

  You probably don't, but hey, it's a nice little tool. I was mostly just
  unhappy with the available options for web scraping, as most if not all of
  them require you to write at least some code yourself. I wanted a reasonably
  general solution that just worked from the command line.


## How does it work?

  Spatula runs on Python 2.7 and depends on `lxml` and `requests`. It just
  makes a request for the HTML content of the page, and then parses it based on
  the given parameters.


## Instructions

  Let's say I want all of the bolded text at `www.example.com`. I'd just run:

  ```
  python spatula.py "http://www.example.com" -s "strong"
  ```

  Maybe I want all of the hyperlink URLs from the Wikipedia homepage:

  ```
  ./spatula.py "http://wikipedia.com" -s "a" -a "href"
  ```
  *Note: Using the `./` notation may require running `chmod +x spatula.py`,
  depending on your system. This also may depend on the path to your python
  executable. When in doubt, use the explicit `python` syntax above.*

  If you want to know more about the ins and outs of the application, just run:

  ```
  python spatula.py -h
  ```
