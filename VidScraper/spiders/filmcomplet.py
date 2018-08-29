import scrapy

class FilmComplet(scrapy.Spider):
    name = 'filmcomplet'

    def start_requests(self):
        urls = ['http://filmcomplet.la']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        affiches = response.css('.affiche::text').extract()
        yield affiches