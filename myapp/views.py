from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autenticar al usuario automáticamente después del registro
            return redirect('home')  # Redirigir a la página principal después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
