from django.http import HttpResponse
from django.shortcuts import render

from .models import Item

# Create your views here.


def index(request):
    item_list = Item.objects.all()
    return HttpResponse(item_list)


def item(request):
    return HttpResponse('This is an item view')