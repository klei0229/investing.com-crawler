import scrapy

##To do's:

##I GOT BLOCKED FIND A WAY TO USEA DOWNLOAD DELAY AND MAYBE HIDE COOKIES


class fa_investing(scrapy.Spider):
	#DOWNLOAD_DELAY = 3
	name = 'fa_investing'
	start_urls = ['https://www.investing.com/news/cryptocurrency-news']
	#start_urls = ['https://www.investing.com/news/stock-market-news']

	## Anti-ban measurements

	#Cookies are enabled True by default
	COOKIES_ENABLED = False
	#Download delay to not get banned
	DOWNLOAD_DELAY = 1.5
	AUTOTHROTTLE_ENABLED = True
	AUTOTHROTTLE_START_DELAY = 2
	AUTOTHROTTLE_TARGET_CONCURRENCY = 6

	## Anti-ban measurements

	def parse(self,response):
		SET_SELECTOR = '.articleItem'
		for investing in response.css(SET_SELECTOR):
			TITLE_SELECTOR = 'a.title ::text'
			AUTHOR_SELECTOR = 'div.articleDetails span ::text'
			DATE_SELECTOR = 'div.articleDetails span.date ::text'
			LINK_SELECTOR = 'a.title ::attr(href)'
			PARA_SELECTOR = 'p ::text'
			yield{
		 		'title': investing.css(TITLE_SELECTOR).extract_first(),
		 		'author': investing.css(AUTHOR_SELECTOR).extract_first(),
		 		'date': investing.css(DATE_SELECTOR).extract_first(),
		 		'links': investing.css(LINK_SELECTOR).extract_first(),
		 		'paragraph': investing.css(PARA_SELECTOR).extract_first(),
		 		}
		##Becareful with mixing identation and tabs
		NEXT_PAGE_SELECTOR = 'link[rel="next"]::attr(href)'
		next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
		if next_page:
			yield scrapy.Request(
				response.urljoin(next_page),
				callback=self.parse
				)