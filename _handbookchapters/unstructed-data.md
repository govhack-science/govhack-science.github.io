Unstructured data covers much of the data you will come across - from data buried in PDFs and web sites, to mining data from social networks, but it all requires analysis to extract meaning. There are many tools for getting at the data - see the previous section on [scraping data](#Scraping_data_from_PDFs_and_the_web) for a range of tools - but the Sunlight Foundation's [Text Analysis in Transparency](http://overview.ap.org/blog/2013/05/video-text-analysis-in-transparency/) talk is a great introduction to that world of text analysis and natural language processing.


# Extracting meaning from text

Once you have your data in a nicer format you may well need to tackle the problem of pulling something meaningful out of it. Fortunately, there are a lot of good analysis and natural language processing libraries around these days that will allow you to [automatically find the meaningful keywords in a body of text](http://thetokenizer.com/2013/05/09/efficient-way-to-extract-the-main-topics-of-a-sentence/).

Natural language processing may be a bit of a heavy topic to dive into during a hackathon, but if you're feeling brave there are a few [good](http://www.vikparuchuri.com/blog/natural-language-processing-tutorial/) [tutorials](http://idibon.com/natural-language-processing-tutorial-with-ebert/) on the subject to get you started (if you'd like some more academic articles check [this StackOverflow question](http://stackoverflow.com/questions/11892128/tutorials-for-natural-language-processing)).

As always, there are web-based tools - such as [TextRazor](http://www.textrazor.com/) and [Yahoo Content Analysis](https://developer.yahoo.com/contentanalysis/) - that may be able to save you the trouble of diving into code and learning too much about the theory and practice of NLP whilst time is tight.

There are a surprising number of good NLP libraries around for all of the major languages though:

Java has [OpenNLP](https://opennlp.apache.org/) and [Apache UIMA](http://uima.apache.org/); Python has [NLTK](http://www.nltk.org/), [pattern](https://github.com/clips/pattern), and [TextBlob](http://textblob.readthedocs.org/en/dev/); and [this StackOverflow question](http://stackoverflow.com/questions/22904025/java-or-python-for-natural-language-processing) has a good dicussion of NLP libraries for both languages.

In .NET-land the Standford NLP Group have made parts of [their software available](http://sergey-tihon.github.io/Stanford.NLP.NET/), and [SharpNLP](https://sharpnlp.codeplex.com/) and [Adodit NLP](http://nlp.abodit.com/) are worth a look too.

Beyond the world of NLP you might consider going straight to a search engine that provides similar text interrogation capabilities along with a database to store your data and APIs to query it. [Solr](http://lucene.apache.org/solr/) and [Elastic](https://www.elastic.co/) (formerly ElasticSearch) are pretty well know in this space - but [Sphinx](http://sphinxsearch.com/) and [Constellio](http://constellio.com/?lang=en) are worthy entries.

Lastly, for a spot of lightweight text mining [Latent Semantic Analysis in Ruby](http://blog.josephwilk.net/ruby/latent-semantic-analysis-in-ruby.html) and [Simple Text Mining with R](http://www.r-bloggers.com/simple-text-mining-with-r/) will point you in the right direction.


# Visualising unstructured text

Being able to visualise unstructured information is key to making sense of it - be it a word tree of a text blob, a whole web page, or a social media feed - tools like [Word Tree](http://www.jasondavies.com/wordtree/), [Overview](https://www.overviewproject.org/), and even [Google Charts](https://developers.google.com/chart/interactive/docs/gallery/wordtree) will help you turn out some quick visualisations. On the academic end of the spectrum the National Science Foundation have made their [Jigsaw](http://www.cc.gatech.edu/gvu/ii/jigsaw/) toolbox available.

Check out [See Text in Whole New Way: Text Visualization Tools](https://blogs.princeton.edu/etc/2012/08/16/see-text-in-whole-new-waytext-visualization-tools/) from Princeton University for a range of other tools.
