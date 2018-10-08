import random
import urllib.request
import os


url = 'https://softech.kg/image/cache/catalog/Products/Phones/Xiaomi/Mi A2 Lite/black_phone-800x600-product_popup.png'
url22 = 'https://myphone.kg/cache/files/market/2357.jpg_w250_h150_resize.jpg'

urls = [url,url22]

path_softech = 'D:/polygon/python/work/catalog/envi/parser/sitecrawler/sitecrawler/spiders/static/cache/catalog/Products/Phones'
path_myphone = 'D:/polygon/python/work/catalog/envi/parser/sitecrawler/sitecrawler/spiders/static/cache'

def make_directory(url, path):
    file_name = url.split('/')[-1]
    subdir = url.split('/')[-2]
    subsubdir = url.split('/')[-3]
    
    path += '/' + subsubdir
    if not os.path.exists(path):
        os.makedirs(path)

    full_path = path +'/' + subdir
    if not os.path.exists(full_path):
        os.makedirs(full_path)

    download_image(url, full_path, file_name)

        
def download_image(url, full_path, file_name):
    r = requests.get(url, allow_redirects=True)
    open(fullname, 'wb').write(r.content)

for url in urls:
    folder_type = url.split('/')[0:3]

    if(folder_type[2] == "myphone.kg"):
        make_directory(url, path_myphone)
        print("this is myphone")
    if(folder_type[2] == "softech.kg"):
        make_directory(url, path_softech)
        print("this is softech")

