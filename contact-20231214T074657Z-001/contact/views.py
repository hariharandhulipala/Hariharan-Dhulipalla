from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactCreate
from django.http import HttpResponse


def index(request):
    shelf = Contact.objects.all()
    return render(request, 'contact/contactsapp.html', {'shelf': shelf})

def upload(request):
    upload = ContactCreate()
    if request.method == 'POST':
        upload = ContactCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return render(request, 'contact/popup.html')
            # return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'contact/upload_form.html', {'upload_form':upload})
