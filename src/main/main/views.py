from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from phones.models import Phone
from django.template import loader
from urllib import request


def index(request):
    maintitle = 'This is main title'
    return render(request,'main/index.html',{ 'maintitle': maintitle })