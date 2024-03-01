from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required 
from django.urls import reverse
from django.contrib import messages
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email=form.changed_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password , email=email)
                if user is not None:
                    login(request, user)
                    return redirect('/')
            else:
                messages.add_message(request,messages.ERROR,'The password or username is incorrect')
                return redirect('/')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'account/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def singup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'You have successfully registered')
                return redirect('/')
            else:
                messages.add_message(request,messages.ERROR,'Something went wrong ! Try again')
        
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'account/singup.html',context)
    else:
        messages.add_message(request,messages.ERROR,'You have already registered')
        return redirect('/')
        