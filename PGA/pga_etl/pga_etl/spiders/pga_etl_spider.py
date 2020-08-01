from scrapy import Spider 
from scrapy.selector import Selector 

from pga_etl.items import PgaEtlItem

# Define the Spider class for PGA stat extraction
class PgaEtlSpider(Spider):
    name = "pga" 
    allowed_domains = ["pgatour.com"] # define the official PGA site
    start_urls = ["https://www.pgatour.com/content/pgatour/stats/stat.159.y2020.eon.t525.html"] # Define the page containing the off the tee stats for 3M Open  

    def parse(self, response):
        stats = Selector(response).xpath('//*[@id="statsTable"]//tbody//tr') 

        for stat in stats: 
            statistics = PgaEtlItem()
            statistics['rank'] = stat.xpath('td[1]/text()').extract()[0]
            statistics['name'] = stat.xpath('td[3]/a/text()').extract()[0]
            statistics['distance'] = stat.xpath('td[5]/text()').extract()[0] 
            
            statistics['tournament'] = "3M Open" # For simplicity this is manually entered, later iterations will cycle through multiple tournamnets
            yield statistics