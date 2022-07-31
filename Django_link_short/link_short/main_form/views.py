from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm, LinkForm
import pyshorteners

userinfo_global='AnonymousUser'

def registerPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'main_form/register.html', context)


def loginPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')



            user = authenticate(request, username=username, password=password)


            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'main_form/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    error=''

    if request.method == 'POST':
        form = LinkForm(request.POST)
        form_change = form.save(commit=False)
        user_info = form.cleaned_data['user_info']
        link_short = form.cleaned_data['link_short']
        link = form.cleaned_data['link_info']
        userinfo_global='AnonymousUser'
        if (len(request.user.username)>1):
            userinfo_global = request.user.username
        form_change.user_info = userinfo_global
        form_change.link_short = pyshorteners.Shortener().tinyurl.short(link)

        form_change.save()
        return redirect('history')

        # if form.is_valid():
        #     inst = form.save(commit=False)
        #     if not inst.link_short:  # or incorrect
        #         inst.data["link_short"] = "TEST!!!"
        #     inst()
        #     return redirect('history')


    form = LinkForm()
    contex = {
        'form': form,
        'error': error,
              }
    return render(request,'main_form/home.html',contex)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def history(request):
    #links = Shortcut_link.objects.all()
    links = Shortcut_link.objects.order_by('-id')
    userinfo_global = 'AnonymousUser'
    if (len(request.user.username) > 1):
        userinfo_global = request.user.username
    links = Shortcut_link.objects.filter(user_info=userinfo_global).order_by('-id')
    return render(request, 'main_form/history.html', {'title': 'Главная страница сайте', 'links': links})
