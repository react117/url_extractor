# Url Extractor

This custom spider routine scrapes and lists all the urls from a website given the base-url.

### Setup

1. Install Scrapy. `https://docs.scrapy.org/en/latest/intro/install.html`

2. Clone the repo.

3. Go through the object (`/items.py`) and the spider (`/url_extractor/spiders/url_extractor.py`) file. It should be straight forward.

4. I have scraped 3 websites and saved the respective urls into 3 separate csv. You can find my scrapped result data in `/output` folder.

### Usage

1. Open Terminal.

2. Go to the `url_extractor` directory.

3. Run `scrapy crawl urlextractor -a start_urls="http://fundrazr.com/,https://www.anandabazar.com,https://www.data-blogger.com/" -o output/links_multi.csv -t csv`. By default the extracted result will be stored in `links_multi.csv` located in the `/output` directory. You can change the csv file name  and location at will.

4. This spider will accept multiple comma separated links as an argument named `start_urls`. It will then extract the list of urls from all of them at one go.

### Known Issue

Among the 3 sites I have tested, for 2 sites the extractor is running in an infinite loop. Means it is listing all the urls but instead of stopping there, it starts from the beginning, resulting in duplicate urls in the csv.

### Changelog

Please see this [changelog](https://github.com/react117/url_extractor/blob/master/CHANGELOG.md) to know about the updates.
