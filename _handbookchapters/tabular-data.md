# Working with tabular data

At its simplest tabular data is data that is stored in rows and columns, either in a flat file or a database, and is usually comprised of simple alphanumeric values. CSV/TSV, JSON, XLS(X), and XML are some of the more common formats you'll find tabular data in, though unfortunately it does still often appear in non machine-readable formats like PDF and DOC and most first be extracted and cleaned before being used.

## Converting between data formats

There's a good chance that you're going to want to convert your data from the format you've found into something a little more modern and useful (like JSON). [Mr. Data Converter](http://shancarter.github.io/mr-data-converter/) is a simple web-based tool for coverting from Excel, CSV, and TSV to JSON, HTML, MySQL, PHP, Python, Ruby, and more.

For batching up the conversion process to run across many datasets consider the [dataconvert](http://okfnlabs.org/dataconverters/#source-data-formats-supported) command-line tool developed by [OKFN Labs](http://okfnlabs.org/) for converting from CSV, XLS(X), and JSON to CSV.

If you need even more control consider the Python libraries [pandas](http://pandas.pydata.org/) (which provides a whole data analysis and modelling framework as well), [tablib](https://tablib.readthedocs.org/en/latest/), or any of the [Science and Data Analysis](https://github.com/vinta/awesome-python#science-and-data-analysis) libraries listed on [Awesome Python](https://github.com/vinta/awesome-python).

## Cleaning your data

If your data has had humans involved in entering it then it's probably fully of all sorts of small variations in how the data have been entered that you'll need to clean up before it becomes machine-readable. Fortunately, there are a couple of great tools.

[OpenRefine](http://openrefine.org/) (formerly Google Refine) is a powerful desktop tool for cleaning messy data, transforming it between different tabular data formats, and even integrates with web services via some simple connectors so you can, for example, geocode a bunch if addresses using Google direclty in OpenRefine. Check out the School of Data's simple [tutorial on using OpenRefine](http://schoolofdata.org/2013/07/15/openrefinelodrefine-a-power-tool-for-cleaning-data/) to see it in action.

Depending on how badly munged your data is a simple old spreadsheet application may get you most of the way to having clean data - as per the excellent [A Gentle Introduction to Data Cleaning](http://schoolofdata.org/courses/#IntroDataCleaning) series from the School of Data. Their [Cleaning Data with Spreadsheets](http://schoolofdata.org/handbook/recipes/cleaning-data-with-spreadsheets/) walkthrough may also fit the bill.

If out-of-the-box tools aren't cutting it and you need to dive into code take a look back at some of the Python libraries, like [pandas](http://pandas.pydata.org/), that we recommended in [Converting between data formats](#Converting_between_data_formats). If you're feeling brave take a look at [dedupe](https://github.com/datamade/dedupe), which leverages machine-learning to perform de-duplication and cleansing of data.

And if all else fails you can always fall back to reliable command-line tools like grep, awk, and sed combined with regular expressions. If you need to upskill your regex foo [Debuggex](https://www.debuggex.com/) and [Regexpr](http://regexper.com/) should set you on the right path.

## Analysing tabular data

So you've got a nice clean dataset and now you want to do some analysis on it to understand if reality matches your hypothesis!

### Spreadsheets

Sometimes the simplest tools are the best and a spreadsheet is all you need - Excel, afte rall, is the world's most widely used IDE!

The School of Data has an excellent tutorial [Using Excel to do precision data journalism](http://schoolofdata.org/2013/04/24/using-excel-to-do-precision-journalism-an-update-from-the-school-of-data-journalism-in-perugia/). If you really need to get back to first principles their [Data Fundamentals](http://schoolofdata.org/courses/#DataFundamentals) series would be well worth a look.

The Sunlight Foundation has a set of good videos as an intro to [Data Visualisation in Google Docs](http://training.sunlightfoundation.com/module/data-visualizations-google-docs/) which also covers analysis. And finally, check out [this rundown of Excel plugins](http://www.clickz.com/clickz/column/2265548/5-free-excel-addins-to-help-digital-marketers-decipher-big-data) for analysing and visualising data.

### Databases

When datasets get larger, or the analysis requirements get more complex, you'll probably find yourself reaching for a database to do the heavy lifting.

The School of Data has a neat little tutorial on [Using SQL for Lightweight Data Analysis](http://schoolofdata.org/2013/03/26/using-sql-for-lightweight-data-analysis/) that'll get you started. If you're playing in PostgreSQL you may find its [window functions](http://www.postgresql.org/docs/9.4/static/tutorial-window.html) of great use to perform calculations across sets within your data.

For a deep dive on data analysis in PostgreSQL, R, and Python check out [this blog post](R, Python, PostgreSQL (and more): A data science workflow example) from Zev Ross.

### R (Arrr!)

R provides a platform for advanced data analysis to let you discover and visualise trends even in large datasets. If you're new to R you should start with [The Guerilla Guide to R](http://www.r-bloggers.com/the-guerilla-guide-to-r/), [basic statistics and graphs in R](https://people.ifm.liu.se/marjon/R_intro_solutions.pdf), and the [official Introduction to R](http://cran.r-project.org/doc/manuals/R-intro.html). To ease the learning curve check out some of the IDEs for R - [RStudio](http://www.rstudio.com/), [Rattle](http://rattle.togaware.com/), and [Deducer](http://www.deducer.org/pmwiki/pmwiki.php?n=Main.DeducerManual).

The true value of R lies in its huge array of libraries and addons, such as [bigvis](http://blog.revolutionanalytics.com/2013/04/visualize-large-data-sets-with-the-bigvis-package.html) (visualise up to 10 million data points in mere seconds) and the big list of [10 R packages I wish I knew about earlier](http://blog.yhathq.com/posts/10-R-packages-I-wish-I-knew-about-earlier.html).

To get started with charting in R check out the handy [Getting Started with Charts in R](http://flowingdata.com/2012/12/17/getting-started-with-charts-in-r/) guide, [Simple charts in R tutorial](http://chartsnthings.tumblr.com/post/36978271916/r-tutorial-simple-charts), or some fun [putting pictures of Pokemon where their power level is on an X/Y axis](http://www.r-bloggers.com/to-plot-them-is-my-real-test/).

When it comes to sharing your analysis with the world check out [Knitr](http://yihui.name/knitr/), for quick and easy report generation, [googleVis](https://github.com/mages/googleVis) for making R and Google Charts talk nicely, and [Shiny](http://shiny.rstudio.com/) for a full-blown web app framework for R to turn your awesome analyses into a shiny interactive web app (such as [this demo](http://blog.ouseful.info/2012/11/28/quick-shiny-demo-exploring-nhs-winter-sit-rep-data/)).

## Visualising tabular data

We've already touched on visualisation in previous section on [Resources for building data visualisations](http://localhost:9000/#data-visualisation-and-infographics-for-fun-and-profit-resources-for-building).
