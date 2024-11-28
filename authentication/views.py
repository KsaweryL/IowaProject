from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm
from django.contrib import messages
from django.core.management import call_command

# Create your views here.
def log_in(request):

    # Checking if the user is logged in
    # If so - redirect them to the page with the message list
    if request.user.is_authenticated:
        return redirect("view_tasks")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # Using Django's built-in authentication system
            # to check if the user exists in the database
            user = authenticate(
                request,
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password")
            )
            # If the user exists - log them in
            # and redirect to news page
            if user is not None:
                login(request, user)
                return redirect("view_tasks")
            # If they do not exist or the data sent is incomplete - send it
            # back to the customer with the data form
            else:
                error = "error"
                context = {"form": form, "error": error}
                return render(request, "authentication/login.html",context)
        else:
            error = "error"
            context = {"form": form, "error": error}
            return render(request, "authentication/login.html",context)
    else:
        context = {"form": LoginForm()}
        return render(request, "authentication/login.html",context)

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')
    
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/register_user.html', {'form': form})