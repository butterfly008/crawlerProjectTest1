import scrapy


class MyItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()

class QuotesSpider(scrapy.Spider):
    name = "wsj_spider"
    
    
    keyword = input("What do you search for in business insider? ")
    start_urls = ['https://www.businessinsider.com/s?q=Elon Musk'& keyword]
  
    

    def parse(self, response):
        item = MyItem()
        #all_divs = response.css('article.hed-summ')
        all_divs = response.css('div.search-result')
            
        for divvs in all_divs:
            
            
            #item['text'] = divvs.css('div.text-wraper p.summary::text').extract()
            item['link']= divvs.css('h3 a::text').get()
            item['title']= divvs.css('a::attr(href)')[0].get()
           
            item['author']= divvs.css('li.author-byline::text').get()
            item['date'] = divss.css('li.river-post__date get::text').get()
            item['text'] = divvs.css('div.excerpt::text').get()
            
            
            yield item
  
 
  
    #for divvs in all_divs:
            
            #item['text'] = response.css('p.summary::text').extract_first()
			#yield item
		
		
