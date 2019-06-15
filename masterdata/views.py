from django.shortcuts import render
from django.http import HttpResponse
from masterdata.models import Movie
# Create your views here.


def index(request):
    mani ="manikandan"

    obj = Movie.objects.all()


    return render(request, 'index.html',locals())

    # return HttpResponse("Hello, world. You're at the polls index.")