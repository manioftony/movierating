from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    
    return render(request, 'index.html',locals())

    # return HttpResponse("Hello, world. You're at the polls index.")