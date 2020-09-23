from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import MovieShort


def index(request):
    # shorts = MovieShort.objects.all()
    #模仿大与3星(7分)
    shorts = MovieShort.objects.filter(score__gt=7.0)
    return render(request, 'shortlist.html', locals())


def search(request, value):
    shorts = MovieShort.objects.filter(short__icontains=value)
    return render(request, 'shortlist.html', locals())