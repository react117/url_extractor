### Synopsis

This custom spider routine scrapes and lists all the urls from a website given the base-url.

### How to replicate my result

1. Install Scrapy. `https://docs.scrapy.org/en/latest/intro/install.html`

2. Clone the repo.

3. Go through the object (`/items.py`) and the spider (`/url_extractor/spiders/url_extractor.py`) file. It should be straight forward.

4. I have scraped 3 websites and saved the respective urls into 3 seperate csvs. You can see my scrapped result data in `/output` folder.

5. To replicate my results, please open your terminal, go to the `url_extractor` directory and run `scrapy crawl urlextractor -o output/links_abp.csv -t csv`. You can change the csv file name at will.

### Known Issue

Among the 3 sites I have tested, for 2 sites the extractor is running in an infinite loop. Means it is listing all the urls but instead of stopping there, it starts from the beginning, resulting in duplicate urls in the csv.
