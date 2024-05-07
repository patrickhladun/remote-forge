from django.shortcuts import render
from apps.user.models import Talent


def home(request):
    return render(request, 'base/home.html')


def about(request):
    talents = Talent.objects.all()
    return render(request, "base/about.html", {"talents": talents})