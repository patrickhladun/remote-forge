from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import RequestContext
from apps.user.models import Talent
from .forms import ContactForm, JobSearchForm
from django.core.mail import send_mail


def home(request):
    talents = Talent.objects.filter(is_published=True)
    form = JobSearchForm()
    
    if request.GET:
        form = JobSearchForm(request.GET)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            location = form.cleaned_data['location']
            query_string = '?'
            if keyword:
                query_string += f'keyword={keyword}&'
            if location:
                query_string += f'location={location}&'
            return redirect(reverse('job-list') + query_string)
    
    return render(request, 'base/home.html', {"talents": talents, "form": form})

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