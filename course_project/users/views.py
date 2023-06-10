from django.contrib.auth import authenticate, login, logout
from icarus.forms import SignupForm , LoginForm
from django.shortcuts import render, redirect
from icarus.models import User


from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")
    
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, email=email, password=password)
                username = username
                return redirect('/icarus/?username=' + username,{'username':username})

                # User credentials are valid, redirect to success page
                #return render(request, 'users/user.html', {'username':username,
                 #                                          'email':email})
            except User.DoesNotExist:
                # User credentials are invalid, show error message
                form.add_error('username', 'Invalid Credentials!')
                
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
                                                

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'home' with the name of your desired redirect URL
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

