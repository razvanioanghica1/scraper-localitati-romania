# -*- coding: utf-8 -*-
import scrapy


class JudeteOraseSpider(scrapy.Spider):
    name = 'judete_orase'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://ro.wikipedia.org/wiki/Liste_de_localit%C4%83%C8%9Bi_din_Rom%C3%A2nia_grupate_pe_jude%C8%9Be']

    def parse(self, response):
        urls = response.css('p b a::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)

    
    def parse_details(self, response):
        yield {
            'judet' : response.css('h1::text').extract_first() ,
            'orase' : response.css('#mw-content-text > div > table > tr > td:nth-child(1) > a::text').extract()
        }
