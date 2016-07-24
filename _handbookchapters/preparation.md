Whilst you're not allowed to actually work on your project until the weekend of GovHack itself, that doesn't mean you can't be preparing and learning new skills and tools beforehand.

## Become a data scientist in an hour

There's so much more to working with data than taking your nicely formatted dataset and throwing it at a software package that will generate pretty graphs, or widgets, or maps out of it. That's just the easy bit - what does your data **actually** mean?

There are three basic rules to follow when doing data science:

1. *Have a hypothesis* - Always start with a basic hypothesis and keep it forefront in your mind. Don't let yourself get distracted by the shiny tools and end up realising you've made something pretty that doesn't actually answer your original question or prove your hypothesis.

2. *Have the right tools* - Find the right tools for the job - keep on scrolling down for a wealth of tools for dealing with all sorts of different types of data.

3. *Analyse and present your findings* - Be upfront and honest in presenting your project. Did you meet your original goal? Was your original hypothesis valid? How did you iterate to get to the final version?

If you'd like to hone your knowledge check out these handy resources:

### Data Science
* The *"Understanding Data"* and *"Delivering Data"* chapters of the (free) [Data Journalism Handbook](http://datajournalismhandbook.org/).

### Visualisation
* [Visualize This: The FlowingData Guide to Design, Visualization, and Statistics](https://booko.com.au/works/955519) by Nathan Yau
* [Data Analysis with Open Source Tools](https://booko.com.au/works/1168452) by Philipp K. Janert
* [Data and visualization blogs worth following](http://flowingdata.com/2012/04/27/data-and-visualization-blogs-worth-following/) (FlowingData)

Also - don't miss our [Data visualisation and infographics for fun and profit](#data-visualisation-and-infographics-for-fun-and-profit) section for a wealth of useful resources.

### Statistics
* [Think Stats: Probability and Statistics for Programmers](https://booko.com.au/works/3475110)

![Illustration from the Data Journalism Handbook](../imgs/data-journalism-handbook.gif ""Look at me: still talking when there's [data] science to do!"")

*Illustration from the Data Journalism Handbook, CC BY-SA 3.0*

## On the importance of APIs

There's a good chance that your project is going to need some sort of API to connect up your backend layer or data store to your frontend interface (be it web-based or otherwise). But APIs are hard, right? Not any more! Where once we used to have to roll our own APIs and handle the lowest level operations ourselves now there are a bevvy of tools and resources to help you make an awesome API quickly.

### APIs as a Service

Services like [Mashery](http://www.mashery.com/), [Apigee](https://apigee.com/about/), [ApiAxle](http://apiaxle.com/), and [3scale](http://www.3scale.net/) provide a quick and easy means to bootstrap your API and provide a range of neat features on the side like analytics and easy inspection and diagnosis of API errors.

### Building and designing your own API

If you need to dig a little further down and actually build your own API it's worth taking a bit of time to think about the design of your API. There are some great resources are such as the API Evangelist's guide to [Providing and Consuming APIs](http://apievangelist.com/) and Atlassian's [REST API Design Guidelines](https://developer.atlassian.com/docs/atlassian-platform-common-components/rest-api-development/atlassian-rest-api-design-guidelines-version-1).

[apiblueprint](http://apiblueprint.org/) is well worth a look as a tool that provides both a means of quickly designing an API, as well as automatically generating nice looking documentation.

### Documenting your API

Documenting your API well is crucial if you expect anyone else to use it (including other developers on your team) and the tools available are myriad.

For REST APIs in general check out [Swagger](http://swagger.io/) or [iodocs](https://github.com/mashery/iodocs). In PHP-land [Symfony](http://symfony.com/) (see also - [REST APIs with Symfony2: The Right Way](http://williamdurand.fr/2012/08/02/rest-apis-with-symfony2-the-right-way/)) and [Slim](http://www.slimframework.com/) are worth a look

In Rails-land take a look at [Apipie-rails](https://github.com/Apipie/apipie-rails).
