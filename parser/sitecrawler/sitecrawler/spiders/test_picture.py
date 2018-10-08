import urllib.request
import random


urls = [ 'https://softech.kg/image/cache/catalog/Products/Phones/Meizu/15 /345-800x600-product_popup.jpg'
        ]
def downloader(image_url):
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name)
    urllib.request.urlretrieve(image_url,full_file_name)

for ur in urls:
    downloader(ur)