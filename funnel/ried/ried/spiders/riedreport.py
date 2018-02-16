# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ried.items import Content

class RiedreportSpider(scrapy.Spider):
    name = "riedreport"
    allowed_domains = ['riedreport.com']
    start_urls = [
    'http://riedreport.com',
    #'http://riedreport.com/members-only-3/',
    #'http://riedreport.com/mission1/',
    #'http://riedreport.com/leadership/',
    #'http://riedreport.com/membership/',
    #'http://riedreport.com/newsroom/',
    #'http://riedreport.com/contact/',
    ]

    ## MULTIPLE CLASS EXPRESSION
    ## //div[contains(@class, 'class1') and contains(@class, 'class2')]

    ## YIELD METHOD ###
    ## def parse(self, response):  
    ##    for content in response.xpath('//div[@id="content"]'):
    ##        yield {
    ##            'paragraph': content.xpath('//p/text()').extract(),
    ##        }

    def parse(self, response):
        item = ItemLoader(item=Content(), response=response)

        item.add_value('url', response.url)
        item.add_xpath('title', '//h2/text()')
        item.add_xpath('content', '//p/text()')
        return item.load_item()

    ## NEXT PAGE  ##
    ##    next_page = response.xpath("//li[contains(@class, 'page_item')]/a/@href").extract_first()
    ##    if next_page is not None:r
    ##        next_page = response.urljoin(next_page)
    ##        yield scrapy.Request(next_page, callback=self.parse)