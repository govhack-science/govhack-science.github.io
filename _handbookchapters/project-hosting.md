We've already spoken about how you can submit your project source materials, but you'll more than likely also need a place to host your application on the web.

## Cloud servers

If you're building any sort of web-connected application (be it web, mobile, or a desktop application) you'll need a server to host it on. These days virtual servers are a dime a dozen (and often significantly cheaper than that) - be they a blank box with command line access that you setup yourself (aka [IAAS](http://en.wikipedia.org/wiki/Infrastructure_as_a_service "Infrastructure as a service")), or a [PAAS](http://en.wikipedia.org/wiki/Platform_as_a_service "Platform as a service") solution that gives you click-button access to databases, caching layers, system utilities, monitoring, and analytics services - all with a nice GUI to keep you from having to delve into command line hell.

### Amazon Web Services

Thanks to the generous support of Amazon Web Services we've got $100 vouchers for each GovHack team. Simply [fill out this form](http://www.govhack.org/amazon-web-services/), including your AWS account number and your team page URL from HackerSpace.

There is also a free tier of usage available to all new AWS accounts, see the [AWS Free Tier page](http://aws.amazon.com/free/?nc1=h_l3_su) for more information. If you're part of a startup company you might like to sign up for [AWS Activate](http://aws.amazon.com/about-aws/whats-new/2014/05/14/announcing-new-features-in-aws-activate-startup-blog-startup-spotlight-and-the-amazon-toolbox/).

Those new to AWS should check out the [Getting Started with AWS guide](http://aws.amazon.com/getting-started/).

### NeCTAR

The [National Research Cloud](http://nectar.org.au/research-cloud) (aka NeCTAR) is just like Amazon Web Services, however it is run on open source software ([OpenStack](https://www.openstack.org/)) and is for use by academics and researchers in Australia. In physical terms, NeCTAR spans [eight data centres](https://www.nectar.org.au/news/where-are-nectar-cloud-node-sites-located) around Australia (located at top ranked Higher Education Institutions) which have combined to provide the largest Federated Academic Cloud in the world at 30,000 cores.

Any university student/staff with a valid .edu.au email address can logon right now and use two "small instances / cores" for three months for free. After the initial three month period there is a simple "allocation tab" on the dashboard where you can apply for longer usage or more compute cycles. The allocation form is a simple one page description of your research and how you are using the cloud for that research.

### Azure, Google Compute Engine, et al.

Trying to list all of the options for virtual server hosting would be a fool's errand, so here are just some of the most popular [IAAS](http://en.wikipedia.org/wiki/Infrastructure_as_a_service "Infrastructure as a service") and [PAAS](http://en.wikipedia.org/wiki/Platform_as_a_service "Platform as a service") options at the moment.

Google offers two services in this space - [Google Compute Engine](https://cloud.google.com/compute/) (IAAS) and [Google App Engine](https://cloud.google.com/appengine/) (PAAS). If containerised application development on Docker is your thing they also have [Google Container Engine](https://cloud.google.com/container-engine/) available (in alpha testing).

Speaking of Docker - [Joyent](https://www.joyent.com/) offers some pretty slick support for Docker along with its traditional [IAAS and PAAS offerings](https://www.joyent.com/partners).

For smaller scale IAAS-type services both [DigitalOcean](https://www.digitalocean.com/) and [Linode](https://www.linode.com/) have great offerings from a mere $5/month.

And of coure there's Microsoft's really rather excellent [Azure](http://azure.microsoft.com/en-gb/) services (IAAS/PAAS). You don't even need to be inside the .NET ecosystem to take advantage of them (though it does help a bit).

Lastly, [Heroku](https://www.heroku.com/) has a great PAAS offering if you need some simple out-of-the-box software that's within their ecosystem.

### A word on containerisation (Docker)

Containerisation and, more specifcally [Docker](https://www.docker.com/), is [all the rage right now](http://thomason.io/why-containerization-is-a-key-enabling-technology-for-paas/). If you haven't really run across containerisation before then think of it like server virtualisation on steroids - i.e. In a plain text file you specify the OS you want, the software you'd like installed (Apache, Nginx, Python, whatever), how you want to configure that software, where to find your code (locally, straight from GitHub), and the result is a tiny virtualised server.

Said tiny virtualised server can then be spun up in minutes either on your laptop, in the cloud, or on your team mate's laptops and all of you will have exactly the same build and configuration. Say goodybe to the headaches of different configurations between development and live applications!

[Docker](https://www.docker.com/) is the best project in this space at the moment, and they're busy building a great ecosystem including [a marketplace for containers](https://hub.docker.com/) and [tools for orchestrating multiple containers together into more complex applications](https://docs.docker.com/compose/).

And due to Docker's crazy levels of popularity all of the aforemetnioned cloud server providers (AWS, Google, Azure, ...) have Docker support built-in!


## Static website hosting

If your project, by virtue of its nature, doesn't already have a web presence (e.g. it's a mobile app or a game) then you're very likely going to need host a static website somewhere (i.e. A pile of HTML, CSS, and JavaScript) to give your project a home.

Probably the easiest and fastest way to achieve that at the moment is via [GitHub Pages](https://pages.github.com/) that hosts a website straight out of your GitHub repository. In addition to that, GitHub Pages provides the option to generate a project site from a collection of pre-built themes and to point your own custom domain at your site.

If you prefer to start from scratch (on GitHub Pages or elsewhere) [Bootstrap](http://getbootstrap.com/) and [Foundation](http://foundation.zurb.com/) are the two preeminent responsive frontend web frameworks around these days that cut away a lot of the work of making a site look pretty so you can concentrate on content (and your awesome GovHack project).

Beyond GitHub you could also look at hosting your site for free on [Azure](http://azure.microsoft.com/en-us/documentation/articles/web-sites-publish-source-control/) or creating a static site [on Heroku](http://www.lemiffe.com/how-to-deploy-a-static-page-to-heroku-the-easy-way/).
