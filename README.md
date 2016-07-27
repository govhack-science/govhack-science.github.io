This is the source for the govhack-science website highlighing sciency datasets at [govhack-science.github.io](http://govhack-science.github.io)

Content served by [Jekyll](http://jekyllrb.com/docs/), with layout and nice bits stolen shamelessly from [Rasmus Andersson](https://github.com/rsms/rsms.github.com)



# Planning
[GovHack Data Model](https://www.lucidchart.com/documents/view/d36186be-0c77-4e89-a735-6022a716566a)


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

# Python Tools
We have a few Python tools to help us manage the ingest of data, and generating a static JSON API.

To setup a virtual environment run (from the root directory):
```
virtualenv --system-site-packages venv
. venv/bin/activate
pip install -r python/requirements.txt
```

## Mentors Ingest
This script takes a `.csv` file exported from FormStack and generates a set of new .md files.

To run:
```
. venv/bin/activate
python python/mentors.py
```

The script tries its best to auto-populate the mentor files based on what exists in Jabberwocky (events, organisations, et cetera), but you should *still read the output of the script* to check for any `WARNINGS` you might need to fix up.


## Prizes Ingest
This script takes a directroy of `.csv` file downloaded from Google Drive and generates a set of new .md files.

To run:
```
. venv/bin/activate
python python/prizes.py
```

The script tries its best to auto-populate the prize files based on what exists in Jabberwocky (events, organisations, et cetera), but you should *still read the output of the script* to check for any `WARNINGS` you might need to fix up.


## Datasets Ingest
This script takes a `.csv` file exported from FormStack and generates a set of new .md files.

To run:
```
. venv/bin/activate
python python/datasets.py
```

The script tries its best to auto-populate the dataset files based on what exists in Jabberwocky (events, organisations, et cetera), but you should *still read the output of the script* to check for any `WARNINGS` you might need to fix up.


## Static API
This script *need to be run everytime we change the frontmatter of an .md* file so that we always serve the latest content to govhack.org. This generates one `.json.` file for each Markdown file thanks to the magic of [python-frontmatter](https://pypi.python.org/pypi/python-frontmatter/0.2.1).

At this stage it's a straight conversion from one to the other - with no magic to compose the full entity object, include links to and from it, yet. 

To run:
```
. venv/bin/activate
python python/frontmatter-to-json.py
```

> Tip: If `importError: No module named yaml`, try [this SO](http://stackoverflow.com/questions/1909025/import-error-with-virtualenv). Otherwise the `virtualenv --system-site-packages venv` command should have imported the usual suspects like pyyaml.
