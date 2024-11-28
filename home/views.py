from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def home_page(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'Log in':
            return redirect('login')
        elif action == "Sign up":
            return redirect("sign_up")

    return render(request, 'home/index.html')

def test_page(request):
    return HttpResponse("test")