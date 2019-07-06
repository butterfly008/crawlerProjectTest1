import scrapy


class MyItem(scrapy.Item):
    text = scrapy.Field()


class QuotesSpider(scrapy.Spider):
    name = "wsj_spider"
    start_urls = ['https://www.wsj.com/news/business']

    def parse(self, response):
        item = MyItem()
        all_divs = response.css('article.hed-summ')
            
        for divvs in all_divs:
            item['text'] = divvs.css('div.text-wraper p.summary::text').extract()
            yield item
  
 
  
    #for divvs in all_divs:
            
            #item['text'] = response.css('p.summary::text').extract_first()
			#yield item
		
		
