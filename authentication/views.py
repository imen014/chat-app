from django.shortcuts import render, redirect
from authentication.models import UserMessengerModel
from authentication.forms import UserCreatorForm, Login_form

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



def create_account(request):
    form =UserCreatorForm()
    message = ''
    if request.method == "POST":
        form = UserCreatorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login_user')
        else:
            message = 'form is not valid'
    return render(request, 'authentication/account_created.html', {'form':form, 'message':message})
        
def login_user(request):
    form = Login_form()
    if request.method == "POST":
        form = Login_form(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'authentication/login.html', {'form':form})

@login_required
def home(request):
    user = request.user
    return render(request, 'authentication/home.html', {'user':user})


def logout_user(request):
    logout(request)
    return redirect('login_user')

def delete_users(request):
    users = UserMessengerModel.objects.all()
    users.delete()
    return redirect('home')

def get_users(request):
    users = UserMessengerModel.objects.all()
    return render(request, 'authentication/get_users.html', {'users':users})