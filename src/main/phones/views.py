from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from phones.models import Phone
from django.template import loader
from urllib import request


def index(request):
    phones = Phone.objects.all()
    listphone = []
    listprice = []
    for item in phones:
        listphone.append(item.model_name)
        listprice.append(str(item.price))
  #
    context = {
        'phones': "phone1",
        'phones2': "phone122",
        'phones2': "phone1333"
    }
    
    return render(request, 'phones/templates/phones/index.html', {context})

def detail(request):#, phone_id):
    all_phones = Phone.objects.all()
    
    phones = Phone.objects.filter(id=423)
    listphone = []
    listprice = []
    listurl = []
    
    phone1 = Phone()

    for item in phones:
        phone1.model_name = item.model_name
        phone1.price = item.price
        phone1.url = item.url

        phone1.phone_image = "/media/catalog/Products/Phones/Asus/asus_2/asus-zenfone-2-16gb-ze500cl-white-800x600-product_popup.jpg"
        
        listphone.append(item.model_name)
        listprice.append(str(item.price))
    
    listurl.append('images')

    phone1.url = media
    context = {
        'object': phone1
    }

    print(listurl)
    return render(request, 'phones/templates/phones/detail.html', context )

def results(request,id=1):
    phones = Phone.objects.get(id=id)
    output = ', '.join([phones.url,phones.model_name,str(phones.price),phones.description])
    return HttpResponse(output)


from rest_framework import viewsets
from phones.serializers import PhoneSerializer

class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer