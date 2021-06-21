from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    service = Service.objects.filter()
    portfolio = Portfolio.objects.filter()
    about = About.objects.filter()
    team = Team.objects.filter()
    client = Client.objects.filter()
    social = CompanySocialDetail.objects.filter()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        messages = request.POST['message']
        contact = Contact(name=name, email=email, phone=phone, messages=messages)
        contact.save()
        context = {'service':service, 'portfolio':portfolio, 'about':about, 'team':team, 'client':client, 'social': social, 'message': messages}
        return render(request, 'home.html', context)
    else:
        context = {'service':service, 'portfolio':portfolio, 'about':about, 'team':team, 'client':client, 'social': social,}
        return render(request, 'home.html', context)
   