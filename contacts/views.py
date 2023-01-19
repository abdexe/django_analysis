from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact
# Create your views here.
def contact(request):
    if request.method == 'POST':
      name = request.POST['name']
      surname = request.POST['surname']
      email = request.POST['email']
      message = request.POST['message']
      if message == '':
        messages.error(request,'Please Fill the form')
      else:
        contact = Contact(name=name, surname=surname,email=email,message=message)
        contact.save()
        messages.success(request,'Your request has been sent')
      return redirect('/')
    
    