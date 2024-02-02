from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import *
from .models import Laptop, Classification
from .forms import UpdateForm, AddForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('crud') 
    else:
        form = AuthenticationForm()
    return render(request, 'pages/login.html', {'form': form})
def index(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')

def contact(request):
          return render(request, 'pages/contact.html')


def services(request):
    return render(request, 'pages/services.html')


def techblog(request):
    laptop = Laptop.objects.all()
    language = Programming_Language.objects.all()
    frontend = Frontend_Stack.objects.all()
    framework = Framework.objects.all()
    ide = IDE.objects.all()
    context = {
         'laptop':laptop, 
         'language':language, 
         'frontend':frontend, 
         'framework':framework, 
         'ide':ide, 


    }
    return render(request, 'pages/techblog.html',context)

def crud(request):
    laptop = Laptop.objects.all()
    total_laptop = laptop.count()
    context = {
         'laptop':laptop, 
        'total_laptop':total_laptop, 
    }

    return render(request, 'pages/crud.html', context)

def language(request):
    language = Programming_Language.objects.all()
    total_language = language.count()
    context = {
         'language':language, 
        'total_language':total_language, 
    }

    return render(request, 'pages/language.html', context)

def stacks(request):
    stacks = Frontend_Stack.objects.all()
    total_stack = stacks.count()
    context = {
         'stacks': stacks, 
        'total_stack': total_stack, 
    }

    return render(request, 'pages/stacks.html', context)

def framework(request):
    framework = Framework.objects.all()
    total_framework = framework.count()
    context = {
         'framework': framework, 
        'total_framework': total_framework, 
    }

    return render(request, 'pages/framework.html', context)

def ide(request):
    ide = IDE.objects.all()
    total_ide = ide.count()
    context = {
         'ide': ide, 
        'total_ide': total_ide, 
    }

    return render(request, 'pages/ide.html', context)

def updateLaptop(request, pk):
    laptop = Laptop.objects.get(id=pk)
    form = UpdateForm(instance=laptop)

    if request.method == 'POST':
        form = UpdateForm(request.POST,request.FILES, instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('techblog')
        
    context = {'form':form}
    return render(request, 'pages/update.html', context)


def deleteLaptop(request, pk):
    laptop = Laptop.objects.get(id=pk)
    if request.method == 'POST':
        laptop.delete()
        return redirect('crud')
    
    context = {'laptop': laptop}
    return render(request, 'pages/delete_laptop.html', context)

def addForm(request):
    form = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('techblog')
            
    context = {'form':form}
    return render(request, 'pages/create.html',context)

