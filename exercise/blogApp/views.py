
from django.forms import SlugField
from django.shortcuts import render
from .models import Test
from django.http import HttpResponse, JsonResponse


def index(req):
    tests = Test.objects.all()
    print(tests)
    context ={
        'tests':tests
    }
    return render(req, 'blogApp/index.html', context)


def detail(req, pk):
    tests = Test.objects.get(pk=pk)
    # print(tests)
    context ={
        'tests':tests
    }
    return render(req, 'blogApp/detail.html', context)
