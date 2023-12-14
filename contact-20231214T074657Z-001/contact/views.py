from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactCreate
from django.http import HttpResponse


def index(request):
    shelf = Contact.objects.all()
    return render(request, 'contact/contactsapp.html', {'shelf': shelf})

