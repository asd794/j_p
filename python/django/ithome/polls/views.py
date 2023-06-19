from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello, wolrd. Your're ar the polls index.")

def year_archive(request,year):
    return HttpResponse("ry"+str(year))

def month_archive(request,year,month):
    return HttpResponse("rym"+year+month)

