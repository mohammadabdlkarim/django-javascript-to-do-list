from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/')
    else:
        f = UserCreationForm()
    
    return render(request, 'register/register.html', {'form': f})

