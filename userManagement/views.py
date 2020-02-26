from django.shortcuts import render, redirect

from .models import Users
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from .forms import registerform, userform

def register(request):
    if request.method == 'POST':
        uform = registerform(request.POST)
        cform = userform(request.POST)
        try:
            # checks for any user existance with same username
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'usermanagement/register.html', {'error': 'Error: Username is already taken', 'form': uform, 'cform': cform})
        except User.DoesNotExist:
            # checks for form validation
            if uform.is_valid() and cform.is_valid():
                user = uform.save()
                # holds with data before another save is called
                fuser = cform.save(commit=False)
                fuser.user = user
                fuser.save()
                # gets data from the form
                username = uform.cleaned_data.get('username')
                password = uform.cleaned_data.get('password')
                # authentication
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect("/usermanagement/profile/")

    else:
        # django user
        uform = registerform()
        # fuser model user
        cform = userform()
    context = {'form': uform, 'cform': cform}
    return render(request, "usermanagement/register.html", context)


def user_login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("/")
        else:
            return render(request, "usermanagement/login.html", {"error": "You got your password or username wronged!!!"})
    else:

        return render(request, "usermanagement/login.html")

# log out function -->> redirects to index
def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")

def profile(request):
    pass