from gc import callbacks
from urllib.parse import urljoin
from scrapy import Request

import scrapy


class TupianSpider(scrapy.Spider):
    name = 'tupian'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/meinv/']

    def parse(self, response, **kwargs):
        # print(response.text)
        hrefs=response.xpath('//ul[@class="pic-list2  clearfix"]/li/a/@href').extract()
        for href in hrefs:
            if href.endswith('.exe'):
                continue
            href=response.urljoin(href)

            # print(href)
            yield Request(href,callback=self.parse_image)
        pass

    def parse_image(self, response, **kwargs):
        images = response.xpath('//ul[@id="showImg"]/li/a/@href').extract()
        for image in images:
            # print(image)
            href = response.urljoin(image)
            yield Request(href, callback=self.parse__image)


    def parse__image(self, response, **kwargs):
        image = response.xpath('//img[@id="bigImg"]/@src').extract_first()

        # print(image)

        yield {'image': image}