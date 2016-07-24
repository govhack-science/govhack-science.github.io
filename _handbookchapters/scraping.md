# Scraping data from PDFs and the web

So, somebody gave you a scanned photocopy of the document as PDF? Or a website has some great data, but it's hidden behind an awful JavaScript-heavy interface? No fear - there's some great tools at your disposal to scrape that data and get it into a nicely machine-readable format.

As always, the School of Data have an excellent series on the ins and outs of extracting data from PDFs and scraping websites - [A gentle Introduction into Extracting Data](http://schoolofdata.org/courses/#GentleIntroExtractingData) - with many useful recommendations of the best tools to use for the job.

tl;dr? Well there are a few standout tools...

[Tabula](http://tabula.technology/) is getting a lot of notice for making the process of extracting tabular data from PDFs a (relative) breeze. Download, install, point it at some PDFs and it'll extract any tabula data in them to a nicely machine-readable CSV or XLS file for you. For a more indepth view have a read through [Introducing Tabula](https://source.opennews.org/en-US/articles/introducing-tabula/) (Source news).

[Apache Tika](http://tika.apache.org/), the older man in the scraping PDFs market, is great for extracting text and metadata from a pile of document formats (PDF, XLS, PPT, ...) - even PDFs containing text in scanned images. OUseful, the Practical Data Journalism blog, has a good walkthroguh of [Getting Text Out Of Anything (docs, PDFs, Images) Using Apache Tika](http://blog.ouseful.info/2015/02/09/getting-text-of-anything-docs-pdfs-images-using-apache-tika/).

Worth a mention as well is [PDF Tables](https://pdftables.com/) a web-based tool from the folks behind ScraperWiki that pretty much does what it says on the box - pulls tabular data out of any PDFs you provide.

On the website scraping end of the equation there are a few desktop and web-based tools around - [import.io](https://import.io/), [UiPath](http://www.uipath.com/automate/screen-scraping) (free trial), [Kimono](https://www.kimonolabs.com/), and [80legs](http://80legs.com/) - but sometimes you just need to write code to do it properly.

[Morph.io](https://morph.io/), which arose out of the demise of ScraperWiki, offers a lightweight scraping framework (Python, PHP, Ruby, or Perl) and a whole web platform and community around scrapers (think Heroku for web scraping).

In Python-land there's [Scrapy](http://scrapy.org/) - a neat framework for extracting data from the web with a strong community and easily extensible codebase. You can think of Scrapy as being the next level up from libraries like [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) and [lxml](http://lxml.de/) (which excel at parsing HTML and XML) in that it incorporates higher level concepts of scraping like spiders, selectors, and items.

Likewise, [Scrapekit](http://scrapekit.readthedocs.org/en/latest/) is awesome and includes a range of advanced features such as caching, multi-threading, and logging.

[This Quora post](http://www.quora.com/What-are-some-good-free-web-scrapers-scraping-techniques) has a good thread with suggestions for scraping frameworks in a variety of languages.
