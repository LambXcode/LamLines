from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from . models import UserProfile
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib import messages


# Create your views here.
def index2(request):
    #DISPLAY INFO OF CURRENT SIGNED IN USER
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"), {
                "message": "Login successful"
            })
        else:
            return render(request, "users/login.html",{
                "message": "Invalid username or password"
            })

    return render(request,"users/login.html")


def logout_view(request):
    logout(request)
    return render(request, "users/login.html",{
        "message": "Logged out..."
    })

def my_view(request):
    pass

@method_decorator(login_required, name='dispatch')
class MyView(View):
    def get(self, request):
        # your view code here
        return render(request, 'users/user.html')
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request.method)
        print(form.errors)
        if form.is_valid():
            form.save()  # Save the new user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            # Automatically log the user in after registration
            new_user = authenticate(username=form.cleaned_data['username'], 
                                     password=form.cleaned_data['password1'],
                                     )
            login(request, new_user)
            return redirect('login')
        else:
            print(form.errors)
            messages.error(request, 'There was an error creating your account. Please try again.')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
