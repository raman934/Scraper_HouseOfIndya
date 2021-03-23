import scrapy
from ..items import DemoProjectItem


class HouseOfIndyaSpiderSpider(scrapy.Spider):
    name = 'HOI_spider'
    start_urls = [
    	'https://www.houseofindya.com/zyra/necklace-sets/cat'
    ]

    def parse(self, response):
    	items = DemoProjectItem()

    	product_name = response.css('#JsonProductList p::text').extract()
    	product_raw_imagelink = response.css('#JsonProductList .lazy::attr(data-original)').extract()
    	product_price = response.css('#JsonProductList span+ span').css('::text').extract()
    	product_discount = response.css('.catgItem span::text').extract()
    	product_discounted_price = response.css('#JsonProductList span:nth-child(1)').css('::text').extract()

    	product_clean_imagelink = []
    	for img_url in product_raw_imagelink:
    		product_clean_imagelink.append(response.urljoin(img_url))

    	items['product_name'] = product_name
    	items['image_urls'] = product_clean_imagelink
    	items['product_price'] = product_price
    	items['product_discount'] = product_discount
    	items['product_discounted_price'] = product_discounted_price

    	yield items