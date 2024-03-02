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
            form = CustomLog(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    email = form.cleaned_data.get('email')
                    user=authenticate(request, email=email, password=password)
                    login(request, user)
                    return redirect('/')
            else:
                messages.add_message(request,messages.ERROR,'The password or username is incorrect')
                return redirect('/')
    form = CustomLog()
    context = {'form': form}
    return render(request, 'account/login.html', context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def singup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUser(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request,messages.SUCCESS,'You have successfully registered')
                return redirect('/')
            else:
                messages.add_message(request,messages.ERROR,'Something went wrong ! Try again')
        
        form = CustomUser()
        context = {'form': form}
        return render(request, 'account/singup.html',context)
    else:
        messages.add_message(request,messages.ERROR,'You have already registered')
        return redirect('/')
class CustomUser(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'username',)
class CustomLog(AuthenticationForm):
    class Meta(AuthenticationForm.Meta):
        fields = AuthenticationForm.Meta.fields + ('email', 'username',)