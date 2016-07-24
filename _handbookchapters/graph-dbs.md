# Intro to graph databases

Graph databases were conceived of as a means to make the task of exploring the connections and networks between entities much easier. Whereas in more traditional databases we would have used a from of link table to represent the relationships between entities, that relationship is implicit in a graph database with every entity containing direct pointers to its adjacent entities without the need to expensively compute indexes.

One of the more obvious uses for graph databases are to store and analyse the relationships between people - think Facebook, Twitter, or any web property with a concept of followers or memberships. If you have a problem where you need to quickly and efficiently know how X is connected to Y and via whom, than graph databases are worth a look.

**Tangent Alert!!** While we're talking about networks and relationships we should introduce the concept of "linked data". If you haven't run across the term before (or have, but still don't understand what it means) check out [Linked Data – for the enlightened non-geek reader (or dummies) (or managers)](http://hangingtogether.org/?p=1943) and [A dummy’s introduction to linked data (me being the dummy)](http://mediastandardstrust.org/blog/a-dummys-introduction-to-linked-data-me-being-the-dummy/).

The GovCamp wiki has a [long list of tools](http://govcampau.wikispaces.com/useful+tools) surrounding linked data that may be of use - [Svgvizler](http://dev.data2000.no/sgvizler/) (for SPARQL graphing), [RelFinder](http://www.visualdataweb.org/relfinder.php) (for RDF visual exploration), and [SPARQL Editor](http://openuplabs.tso.co.uk/demos/sparqleditor) (for interactive SPARQL query building) are useful too.


## Graph DB Software

[Neo4j](http://neo4j.com/) is the popular kid on the graph database block and has a wealth of supporting tools and documentation; and a great community.

Getting your data into Neo4j can be as straightforward as throwing a spreadsheet containing your data, along with instructions on how to construct the relationships between the entities in your data, at Neo4j. For details and in-depth instructions see [Importing data into Neo4j – the spreadsheet way](http://neo4j.com/blog/importing-data-into-neo4j-the-spreadsheet-way/) and [Gmail Email analysis with Neo4j – and spreadsheets](http://neo4j.com/blog/gmail-email-analysis-with-neo4j-and-spreadsheets/). Alternatively, you can use the [new in-built ETL functionality](http://www.slideshare.net/maxdemarzi/etl-into-neo4j) from Neo4j 2.1 to load your CSV formatted data in directly - check out the official guide on [importing from PostgreSQL to Neo4j](Import Data Into Neo4j).

But sometimes you just can't escape [writing some code](http://www.slideshare.net/maxdemarzi/etl-into-neo4j) to get the job done, and to that end the official Neo4j website has [curated a list of libaries](http://neo4j.com/developer/language-guides/) for many of the major languages. Neo4j also has a [REST batch import API](http://neo4j.com/docs/milestone/rest-api-batch-ops.html) if you want to get right down to the coalface.

Neo4j isn't the be all and end all of graph databases, and we'd be remiss if we didn't mention the likes of [OrientDB](http://www.orientechnologies.com/), [Titan](http://thinkaurelius.github.io/titan/), and [Stardog](http://stardog.com/).

Many of the graph databases you'll come into contact with can be queried via a common syntax called [Gremlin](https://github.com/tinkerpop/gremlin/wiki) - where Gremlin is to graph databases as SQL is to traditional RDBMS dabatases. Applications can then be written on top of Gremlin, as you would SQL, and become database largely agnostic. Gremlin also supports a simple data browser application to test execution of queries.


## Analysis

### NetworkX (Python)

[NetworkX](http://networkx.lanl.gov/index.html) (from the Los Alamos National Laboratory) is a social network analysis library for Python. With a large range of advanced analysis functions built-in (e.g. finding communities within a graph), and good support for importing data into graph databases. For more see [Introduction to Social Network Analysis with NetworkX](http://www.cl.cam.ac.uk/~cm542/teaching/2011/stna-pdfs/stna-lecture11.pdf).

### R (Arrr!)

**Of course** there are R packages for graph databases!

[Social Network Analysis in R](http://www.slideshare.net/ianmcook/social-network-analysis-in-r),
[Making prettier network graphs with sna and igraph](http://is-r.tumblr.com/post/38240018815/making-prettier-network-graphs-with-sna-and-igraph), and
[RNeo4j](http://nicolewhite.github.io/RNeo4j/) should get you pointing in the right direction.


## Visualisation

Graph databases represent complex networks, so it turns out creating useful visualisation can be a tad hard - for an intro to the subject see [Visualising Networks: Beyond the Hairball](http://www.slideshare.net/OReillyStrata/visualizing-networks-beyond-the-hairball).

### Tree and hierarchy visualisation

What if your network isn't actually a network and more like a tree or straight hierarchy (i.e. it has no interconnections between entities)?

Congratulations, you can use tree visualisations! It'll be faster and far more visually effective than any other options.

[TreeViz](http://www.randelshofer.ch/treeviz/) is a good start if you just need to run it locally (it's a Java app), but D3.js [can also visualise trees](http://bl.ocks.org/mbostock/4063550) (see [this tutorial](http://blog.pixelingene.com/2011/07/building-a-tree-diagram-in-d3-js/) for step-by-step instructions). D3.js also supports enclosure diagrams (aka circle packing) that [may better represet](http://bl.ocks.org/mbostock/4063530) your tree structure than an actual tree would.

### Flow visualisation

But sometimes you care less about the connections in your network and more about the weight those connections have (e.g. the # emails sent between connections) - well for that you want a flow visualisation like a [sankey diagram](http://bost.ocks.org/mike/sankey/) that will visualise the magnitude of flow between nodes in a network

### Other visualisation tools

[NodeXL](http://nodexl.codeplex.com/) for Excel allows you to visualise networks/graphs quickly from right inside Excel.

[Gephi](http://gephi.github.io/) is a great desktop tool for interactive visualisation and exploration platform for networks and hierarchial systems. It comes with many good automatic layout algorithims (even for huge graphs) and can easily handle many types of input file, including [spreadshets of Tweets](http://dfreelon.org/2013/04/26/spreadsheet-converts-tweets-for-social-network-analysis-in-gephi/).

[Cytoscape](http://www.cytoscape.org/) is like Gephi, but more on the 'platform' end of the spectrum. It was originally designed for use in the biological sciences, but has evolved to become a general tool for complex network analysis and visualisation. Cytoscape supports a rich ecosystem of (Java) plugins (aka "Apps") that allow you to customise and extend the base functionality.

[Cytoscape.js](https://github.com/cytoscape/cytoscape.js) Like Cytoscape, but written in JavaScript!

[sigma.js](http://sigmajs.org/) is a simple and elegant JavaScript library solely designed to be aweosme at graph drawing. Give it a JSON blob and it'll spit out a nice looking Canvas or WebGL visualisation of the network. And it also speaks the same formats that Neo4J, Gephi, et cetera can export. Sigma.js also supports [filtering and searching](https://github.com/jacomyal/osdc2012-sigmajs-demo) the visualisations it generates.
