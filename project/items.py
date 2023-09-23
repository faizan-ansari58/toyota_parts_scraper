# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjectItem(scrapy.Item):
    page_url_id = scrapy.Field()
    page_link = scrapy.Field()
    car_model = scrapy.Field()
    main_group = scrapy.Field()
    sub_group = scrapy.Field()
    part = scrapy.Field()
    image_url = scrapy.Field()
    code = scrapy.Field()
    part_number = scrapy.Field()
    production_date = scrapy.Field()
    qty = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
