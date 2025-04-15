import scrapy


class YouxiSpider(scrapy.Spider):
    name = 'youxi'
    allowed_domains = ['4399.com']
    start_urls = ['http://4399.com/']

    def parse(self, response):
        # print(response.text)
        list=response.xpath('/html/body/div[10]/div[1]/div[1]/ul/li')

        for index in list:
            game_name=index.xpath('./a/text()').extract_first()
            # print(game_name)
            yield {
                'name':game_name
            }
        # pass
