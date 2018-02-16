import scrapy

class BrickSetSpider(scrapy.Spider):
	name = 'riedreport'
	allowed_domains = ['riedreport.com']
	start_urls = ['http://riedreport.com']

	def parse(self, response):

		NAME_SELECTOR_DIV = '//*[contains(@id, "contentWrapper")]'
		NAME_SELECTOR_UL = '//ul'

		X_SELECTOR_HEADERS = '//div/h2/text()'
		X_SELECTOR_PARAGRAPHS = '//div/p/text()'
		X_SELECTOR_LISTS = '//ul/li/text()'

		list_exist = response.xpath(NAME_SELECTOR_UL).extract_first()


		for brickset in response.xpath(NAME_SELECTOR_DIV):
			yield {
				'headers': brickset.xpath(X_SELECTOR_HEADERS).extract(),
				'paragraphs': brickset.xpath(X_SELECTOR_PARAGRAPHS).extract(),
			}		
			if list_exist is not None: 
				'list': brickset.xpath(X_SELECTOR_LISTS).extract()