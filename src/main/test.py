#!/usr/bin/env python
import os
import sys


url ='https://softech.kg/image/cache/catalog/Products/Phones/Asus/asus 2/asus-zenfone-2-16gb-ze500cl-white-800x600-product_popup.jpg'
url = url.replace(' ', '_')
print(url)
path = url.split('/')
print(path)


del path[0:4]
imgpath = ['/media']
result = imgpath + path
media = '/'.join(result)
print(media)