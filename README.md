This is the source for the govhack-science website highlighing sciency datasets at [govhack-science.github.io](http://govhack-science.github.io)

Content served by [Jekyll](http://jekyllrb.com/docs/), with layout and nice bits stolen shamelessly from [Rasmus Andersson](https://github.com/rsms/rsms.github.com)



# Planning
[GovHack Data Model](https://www.lucidchart.com/documents/edit/d36186be-0c77-4e89-a735-6022a716566a)


# Documentation
- [Jekyll](https://jekyllrb.com/docs/github-pages/)
- [Liquid Templating Engine](https://shopify.github.io/liquid/)
- [Liquid For Designers](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers)


# Requirements
- Ruby
- RubyGems
- NodeJS
- Python
- Jekyll

# Installation
https://jekyllrb.com/docs/installation/
https://jekyllrb.com/docs/github-pages/

> Our friends at GitHub have provided the github-pages gem which is used to manage Jekyll and its dependencies on GitHub Pages. Using it in your projects means that when you deploy your site to GitHub Pages, you will not be caught by unexpected differences between various versions of the gems. To use the currently-deployed version of the gem in your project, add the following to your Gemfile

> The best way to install Jekyll is via RubyGems. At the terminal prompt, simply run the following command to install Jekyll:

`$ gem install github-pages`

All of the GitHub pages flavour of Jekyll, and its gem dependencies are automatically installed by the above command, so you won’t have to worry about them at all.


# Run
https://jekyllrb.com/docs/usage/

`jekyll serve`

If you receive a message like:

> Could not find gem 'github-pages (= 67)' in any of the gem sources listed in your Gemfile or available on this machine. (Bundler::GemNotFound)

Then it means GitHub has upgraded their `github-pages` gem version, so just run `bundle install` from the root directory to upgrade to the latest set of deps GitHub is using.