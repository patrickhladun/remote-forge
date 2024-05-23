from django.shortcuts import render, redirect
from django.template import RequestContext
from apps.user.models import Talent
from .forms import ContactForm
from django.core.mail import send_mail


def home(request):
    talents = Talent.objects.all()
    return render(request, 'base/home.html', {"talents": talents})

def about(request):
    talents = Talent.objects.all()
    return render(request, "base/about.html", {"talents": talents})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('contact_success')

    else:
        form = ContactForm()

    return render(request, 'base/contact.html', {'form': form})

def contact_success(request):
    return render(request, "base/contact-success.html")


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