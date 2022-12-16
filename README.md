## NOTICE

* (12/22) As heroku has recently removed support for free tier instances the API has been permanently taken offline.

# audiobookcup-dl

While this started as a simple CLI tool to download audiobooks easily from audiobookcup.com,
many potential users were not familier with Python or the CLI which led me to creating
a web app hosted on GitHub Pages and Heroku. To easily download an audiobook with out any
programming prowess, visit [noahcardoza.dev/audiobookcup-dl](https://noahcardoza.dev/audiobookcup-dl/).

## Notice

The site once known as audiobookcup.com is no longer up. I would like to assume that
is in-part, due to this tool. For anyone who hasn't seen the site: there is no way it was
legit. All the audiobooks were watermarked with "This is Audible" and they were trying to
charge users money. As I suspected, providing a tool that broke their business model was
enough to shut them down, for now.

## CLI Usage

Using Python 3.9, running this script is as easy as:

```bash
python main.py "<url>"
```
