from cgitb import text
from email import message
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Carousel, NewsUrl,Section, Services
from django.core.mail import BadHeaderError, send_mail
from django.contrib import messages

def index (request):
    carousel = Carousel.objects.all()
    section2 = Section.objects.all()
    services = Services.objects.all()
    
    context = {
        'carousel': carousel,
        'section' : section2,
        'services' : services
    }
    if request.method == 'POST' :
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        message_body = f'\n {message} \n {phone} \n {name} tomonidan yuborildi {email}'
        if subject and name and email and phone :
            try:
                send_mail(subject, message_body, email, ['rokkidjango@gmail.com'])
                messages.add_message(request, messages.WARNING, 'Xabaringiz yuborildi')
            except BadHeaderError:
                messages.add_message(request, messages.WARNING, 'Xatolik yuz berdi')
        else:
            messages.add_message(request, messages.WARNING, "Barcha q atorlarni to'ldiring!") 
    return render(request, 'index.html', context)

def about (request):
    return render(request, 'about.html')

def contact (request):
    return render(request, 'contact.html')


# register
def register (request):
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            
            if User.objects.filter(email=email).exists():
                message.info (request, 'Email Already')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                message.info (request, 'Username Already')
                return redirect('register')
            else:
                user = User.objects.create_user (username=username, email=email,password=password)
                user.save();
                return redirect('login')
        else:
            message.info(request, 'Password error')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login (request) :
    if request.method =='POST' :
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,auth)
            return redirect
        else :
            message.info (request, 'Credintails invalid')
            return redirect ('login')
    else:   
        return render (request, 'login.html')
    
def news (request):
    return render(request, 'news.html')

def single (request):
    newsurl = NewsUrl.objects.all()
    
    context = {
        'newsurl' : newsurl
    }
    return render(request, 'single.html',context)
