import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lxml import html
from sitecrawler.items import SitecrawlerItem
from scrapy.http import Request
from mysql.connector import MySQLConnection, Error

class SoftechSpider(CrawlSpider):
    name = "softech"
    is_start = False
    val = []
    indexes = 0

    allowed_domains = ["softech.kg"]
    start_urls = (
        'https://softech.kg/phones/', 
    )

    rules = (
        Rule(
            LinkExtractor(restrict_xpaths=[
                '//div[@class="name subcatname"]/a',
                ]),    
            callback='parse'
        ),
        Rule(
            LinkExtractor(allow='https://softech.kg/phones/*'),
            callback='parse_page'
        ),
    )

    def parse(self, response):    
        print("main page")
        for item in response.xpath('//div[@class="name subcatname"]/a'):
            phonesurl = item.xpath("@href").extract()
            print("urls", phonesurl)
            yield scrapy.Request(url=phonesurl[0], callback=self.parse_page_models)

    def parse_page_models(self, response):
        site = response

        for item in site.xpath('//div[@class="product-thumb transition options"]//div[@class="name"]/a'):
            model_url = item.xpath("@href").extract()

            for urlitem in model_url:
                print(urlitem)
                print("url =",urlitem)
                yield scrapy.Request(url=urlitem,callback=self.parse_page)
 
    def parse_page(self, response):
        site = response
        listofitems = []
        model_name = ''
        prices = ''
        url_img = ''
        values = []

        for item in site.xpath('//div[@class="general_info product-info"]'):
            itemd = SitecrawlerItem()
            name = item.xpath('//h1[@class="product-title"]/text()').extract()
            price = item.xpath('//div[@class="price-section"]/span[@class="price-new"]//text()').extract()
            
            model_name = name
            prices = price
            listofitems.append(itemd)

        for item in site.xpath('//div[@class="inner"]/img'):
            imgurli = item.xpath("@src").extract()

            url_img = imgurli

        print(values)

        id = str(self.get_last_id())
        values = [(id, model_name[0], url_img[0], prices[0][:-5], 'None')]
    
        self.insert_into_db(values)

        return listofitems

    def insert_into_db(self,values):
        try:
            conn = MySQLConnection(
                host = "localhost",
                user = "user",
                passwd = "password",
                database = "database")
            cursor = conn.cursor()

            sql = 'INSERT INTO phones_phone (id, model_name, url, price, description) VALUES (%s,%s, %s, %s, %s)'
        
            cursor.executemany(sql, values)
            conn.commit()
            print(cursor.rowcount, "was inserted")
 
        except Error as e:
            print(e)
 
        finally:
            cursor.close()
            conn.close()

    def get_last_id(self):
        try:
            conn = MySQLConnection(
                host = "localhost",
                user = "emil",
                passwd = "Password!@#",
                database = "database")
            cursor = conn.cursor()

            cursor.execute("SELECT COUNT(*) FROM phones_phone")
            rows = cursor.fetchall()
            count = ''
            print('Total Row(s):', cursor.rowcount)
            for row in rows:
                print(row)
                print(row[0])
                count = row[0]
                
            return int(count)+1

        except Error as e:
            print(e)
 
        finally:
            cursor.close()
            conn.close()
