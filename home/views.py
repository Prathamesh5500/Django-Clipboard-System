# views.py
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import LongText
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime ,date

@login_required(login_url='login')
def HomePage(request):
    if request.method == 'POST':
        text = request.POST.get('long_text')
        is_public = request.POST.get('public_checkbox')

        # Set the state based on the checkbox value
        state = 'public' if is_public else 'private'

        # Get the current time without microsecond part
        current_time = datetime.now().strftime('%H:%M:%S')

        # Create a LongText object with the current date and time
        LongText.objects.create(
            user=request.user, username=request.user.username, text=text, state=state, dt=date.today(), tm=current_time
        )
        # Redirect to the same page to avoid form resubmission on refresh
        return redirect('home')

    # Retrieve all private LongText objects for the current user
    private_texts = LongText.objects.filter(user=request.user, state='private')

    return render(request, 'home.html', {'all_texts': private_texts})


def display_public_data(request):
    # Retrieve all public LongText objects from the database in reverse order
    public_texts = LongText.objects.filter(state='public')

    # Send all public texts to the template
    return render(request, 'public_data.html', {'all_texts': public_texts})


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already taken. Please choose a different one.")

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
