from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from tutorial.items import doubanItem
from scrapy.http import Request

class doubanSpider(CrawlSpider):
    name = "douban"
    #allowed_domains = ["douban.com"]
    start_urls =["https://movie.douban.com/top250"]
    urls = 'https://movie.douban.com/top250'
    def parse(self,response):
        #print(response.body)
        item = doubanItem()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        for eachMovie in Movies:
            title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()

            fulltitle = ''
            for eachTitle in title:
                fulltitle += eachTitle
            movieInfo = eachMovie.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = eachMovie.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            if quote:
                quote = quote[0]
            else:
                quote = ""
            print('title',fulltitle)
            print('movieinfo',movieInfo)
            print('star',star)
            print('quote',quote)

            item['title'] = fulltitle
            item['movieInfo'] = movieInfo
            item['star'] = star
            item['quote'] = quote
            yield item

        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        print('nextLink:',nextLink)
        if nextLink:
                nextLink = nextLink[0]
                print('nextlink',nextLink)
                print("url",self.urls )
                yield Request(self.urls +nextLink, callback=self.parse)






