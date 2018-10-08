import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lxml import html
from sitecrawler.items import SitecrawlerItem
from scrapy.http import Request
from mysql.connector import MySQLConnection, Error
from .db_settingsbak import *

class MyPhoneSpider(CrawlSpider):
    name = "myphone"
    is_start = False
    val = []
    indexes = 0
    start_urls = (
        'https://myphone.kg/catalog/cell/apple?all=true',
        'https://myphone.kg/catalog/cell/beeline?all=true',
        'https://myphone.kg/catalog/cell/huawei?all=true',
        'https://myphone.kg/catalog/cell/lenovo?all=true',
        'https://myphone.kg/catalog/cell/samsung?all=true',
        'https://myphone.kg/catalog/cell/senseit?all=true',
        'https://myphone.kg/catalog/cell/xiaomi?all=true', 
    )

    def parse(self, response):    
        print("main page")
        title = []
        price = []
        images = []
        img_url = []

        for url in self.start_urls:
            for item in response.xpath('//div[@class="itemList clearfix"]/div[@class="oneItem"]'):
                title = item.xpath('//div[@class="title"]/a/text()').extract()
                price = item.xpath('//div[@class="price"]/a/text()').extract()
                images = item.xpath('//a[@class="item_image"]//img')
                img_url = images.xpath("@src").extract()

        del title[0:24] # delete not needed parsed titles
        del price[0:1]  # delete price      
        del img_url[0:1] # delete image url

        for img in img_url:
            print(img)

        for model in title:
            print(model)

        for model_price in price:
            print(model_price)

         values = []
        print(self.indexes)
        
        for i in range(len(title)):
            self.indexes = self.indexes + 1
            values.append((str(self.indexes),title[i], 'https://myphone.kg' + img_url[i], price[i][:-4].replace(" ",""),"None"))

        self.insert_into_db(values)
        values.clear()
        self.is_start = True

    def insert_into_db(self, values):
        try:
            conn = MySQLConnection(
                #host = "localhost",
                #user = "user",
                #passwd = "password",
                #database = "database")
                host = DBHOST,
                user = DBUSER,
                passwd = DBPASSWD,
                database = DBDATABASE)
            cursor = conn.cursor()
            #cursor.execute("SELECT * FROM phones_phone")
            if self.is_start == False:
                sql_trunc = 'TRUNCATE database.phones_phone'
                cursor.execute(sql_trunc)
                conn.commit()

            sql = 'INSERT INTO phones_phone (id, model_name, url, price, description) VALUES (%s,%s, %s, %s, %s)'
        
            cursor.executemany(sql, values)
            conn.commit()
            print(cursor.rowcount, "was inserted")
 
        except Error as e:
            print(e)
 
        finally:
            cursor.close()
            conn.close()
 
