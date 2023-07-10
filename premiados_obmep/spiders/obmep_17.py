import scrapy

from premiados_obmep.items import Teacher

class Obmep17Spider(scrapy.Spider):
    name = 'Obmep17Spider'
    edition = '17ª OBMEP'
    year = 2022
    
    start_urls = ['http://premiacao.obmep.org.br/17obmep/verRelatorioProfessoresPremiados.do.htm']

    def parse(self, response):
        awarded_teachers = response.css('table tbody tr')
        for teacher in awarded_teachers:
            yield Teacher(
                name = teacher.xpath('td[3]//text()').get(),
                school = teacher.xpath('td[4]//text()').get(),
                school_type = teacher.xpath('td[5]//text()').get(),
                city = teacher.xpath('td[2]//text()').get(),
                code_state = teacher.xpath('td[1]//text()').get(),
                group = teacher.xpath('td[6]//text()').get(),
                edition = self.edition,
                year = self.year
            )