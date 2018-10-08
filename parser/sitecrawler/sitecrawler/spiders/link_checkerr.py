from mysql.connector import MySQLConnection, Error
from db_settingsbak import *
import random
import urllib.request
import os
import requests

#url = 'https://softech.kg/image/cache/catalog/Products/Phones/Xiaomi/Mi A2 Lite/black_phone-800x600-product_popup.png'
#url22 = 'https://myphone.kg/cache/files/market/2357.jpg_w250_h150_resize.jpg'

path_softech = 'D:/polygon/python/work/catalog/envi/parser/sitecrawler/sitecrawler/spiders/static/cache/catalog/Products/Phones'
path_myphone = 'D:/polygon/python/work/catalog/envi/parser/sitecrawler/sitecrawler/spiders/static/cache'


def make_directory(url, path, real_url):
    file_name = url.split('/')[-1]
    subdir = url.split('/')[-2]
    subsubdir = url.split('/')[-3]
    
    path += '/' + subsubdir
    path = path.replace(' ','_')
    
    if not os.path.exists(path):
        os.makedirs(path)

    full_path = path +'/' + subdir
    full_path = full_path.replace(' ','_')
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    download_image(real_url, full_path, file_name)

        
def download_image(url, full_path, file_name):
    fullname = full_path + '/' + file_name
    full_file_name = fullname.replace(' ','_').encode('utf-8')
    
    urllib.request.urlretrieve(url,full_file_name)

 
def query_with_fetchall():
    try:
        conn = MySQLConnection(
            host = DBHOST,
            user = DBUSER,
            passwd = DBPASSWD,
            database = DBDATABASE)
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM phones_phone")
        rows = cursor.fetchall()
 
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row[2])
            real_url = row[2]
            folder_from_url = row[2]
            folder_type = folder_from_url.split('/')[0:3]
     
            if(folder_type[2] == "myphone.kg"):
                make_directory(folder_from_url, path_myphone, real_url)
            if(folder_type[2] == "softech.kg"):
                make_directory(folder_from_url, path_softech, real_url)
 
     except Error as e:
        print(e)
 
    finally:
        cursor.close()
        conn.close()
 
if __name__ == '__main__':
    query_with_fetchall()

