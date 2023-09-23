import csv
import scrapy
from project.items import ProjectItem


class ProjectSpider(scrapy.Spider):
    name = 'car'

    def start_requests(self):
        # Read the list of start URLs from the CSV file
        link_number_list = []
        link_list = []
        with open("toyota_input_links.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                link_number = row['link_no']
                link = row['subgroup_link']
                link_number_list.append(link_number)
                link_list.append(link)

        for num in range(350000, 400000):
            yield scrapy.Request(url=link_list[num], callback=self.parse, cb_kwargs={'link': link_list[num], 'link_num': link_number_list[num]})

    def parse(self, response, link, link_num):
        car_model = response.xpath('//ul[@class="breadcrumbs"]/li[4]/a/text()').get()
        main_group = response.xpath('//ul[@class="breadcrumbs"]/li[5]/a/text()').get()
        sub_group = response.xpath('//ul[@class="breadcrumbs"]/li[6]/a/text()').get()
        part = response.xpath('//ul[@class="breadcrumbs"]/li[7]/span[2]/text()').get()
        image_url = response.css('div.img_wrapper img::attr(src)').get()
        parts_rows = response.xpath('//table[@class="table"]//tr')

        for parts_row in parts_rows:
            basket_td = parts_row.css('td.table__td.table__td--basket')
            if basket_td.css('a'):
                code = parts_row.xpath('td[1]/text()').get()
                part_number = parts_row.xpath('td[2]/text()').get()
                name = parts_row.xpath('td[3]/text()').get()
                production_date = parts_row.xpath('td[4]/text()').get()
                description = parts_row.xpath('td[5]/text()').get()

                item = ProjectItem(
                    page_url_id=link_num,
                    page_link=link,
                    car_model=car_model,
                    main_group=main_group,
                    sub_group=sub_group,
                    part=part,
                    image_url=image_url,
                    code=code,
                    part_number=part_number,
                    name=name,
                    production_date=production_date,
                    description=description,
                )
                yield item
  

