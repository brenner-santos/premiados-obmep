import scrapy


class AlunosPremiados(scrapy.Item):
    name = scrapy.Field()
    school = scrapy.Field()
    school_type = scrapy.Field()
    city = scrapy.Field()
    code_state = scrapy.Field()
    level = scrapy.Field()
    medal = scrapy.Field()
    position = scrapy.Field()
    year = scrapy.Field()
    edition = scrapy.Field()

class Teacher(scrapy.Item):
    name = scrapy.Field()
    school = scrapy.Field()
    school_type = scrapy.Field()
    city = scrapy.Field()
    code_state = scrapy.Field()
    group = scrapy.Field()
    year = scrapy.Field()
    edition = scrapy.Field()