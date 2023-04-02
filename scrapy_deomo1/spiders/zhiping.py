import json

import scrapy
from scrapy_deomo1.myrequests import SeleniumRequest
from scrapy_deomo1.items import NovelItem
class ZhipingSpider(scrapy.Spider):
    name = 'zhiping'
    allowed_domains = ['17k.com']
    start_urls = ['https://passport.17k.com/login/']
    def start_requests(self):
        yield SeleniumRequest(url=self.start_urls[0],
                              callback=self.parse)
    def parse(self, response, **kwargs):
        a_list = response.xpath('/html/body/div[2]/div/div/div[1]/div[1]/div/div/a')
        # novel_item = NovelItem()
        meta = {}
        for a_item in a_list:
            info_href = 'https:' + a_item.xpath('@href').extract_first()
            image_src = a_item.xpath('./img/@src').extract_first()
            title = a_item.xpath('./p/text()').extract_first()
            # novel_item['title'] = title
            # novel_item['image_src'] = image_src
            # novel_item['info_href'] = info_href

            meta['title'] = title
            meta['image_src'] = image_src
            meta['info_href'] = info_href

            yield scrapy.Request(
                url=info_href,
                callback=self.parse_info,
                meta=meta
            )


    def parse_info(self, response, **kwargs):
        novel_item = NovelItem()
        novel_item['title'] = response.meta['title']
        novel_item['image_src'] = response.meta['image_src']
        novel_item['info_href'] = response.meta['info_href']
        introduction = response.xpath('//p[@class="intro"]/a/text()').extract_first()
        novel_item['introduction'] = introduction
        yield novel_item

