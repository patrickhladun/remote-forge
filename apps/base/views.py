from django.shortcuts import render
from django.template import RequestContext
from apps.user.models import Talent


def home(request):
    talents = Talent.objects.all()
    return render(request, 'base/home.html', {"talents": talents})

def about(request):
    talents = Talent.objects.all()
    return render(request, "base/about.html", {"talents": talents})

def privacy(request):
    return render(request, "base/privacy.html")

def terms(request):
    return render(request, "base/terms.html")

def error404(request, *args, **argv):
    response = render('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def error500(request, *args, **argv):
    response = render('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response