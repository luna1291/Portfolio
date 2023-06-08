from django.shortcuts import render, redirect
from django.http import HttpResponse, BadHeaderError, HttpResponseRedirect
from django.utils.html import strip_tags

from .models import AboutPage, HomePage, Serts
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def index(request):
    quote = HomePage.objects.all()
    text = HomePage.objects.all()
    photo = HomePage.objects.all()
    data = {
        'quote': quote,
        'text': text,
        'photo': photo
    }
    return render(request, "main_app/index.html", data)


def about(request):
    id = AboutPage.objects.all()
    about_shert = AboutPage.objects.all()
    header = AboutPage.objects.all()
    topbox = AboutPage.objects.all()
    header2 = AboutPage.objects.all()
    botbox = AboutPage.objects.all()
    image = AboutPage.objects.all()
    id2 = Serts.objects.order_by()
    sert_name = Serts.objects.all()
    serts = Serts.objects.all()
    data = {
        'id': id,
        'about_shert': about_shert,
        'header': header,
        'topbox': topbox,
        'header2': header2,
        'botbox': botbox,
        'image': image,
        'id2': id2,
        'sert_name': sert_name,
        'serts': serts
    }
    return render(request, "main_app/about.html", data)
print('ok')

def contacts(request):
    return render(request, "main_app/contacts.html")

