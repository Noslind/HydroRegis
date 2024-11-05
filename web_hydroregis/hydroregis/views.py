from django.shortcuts import render, redirect
# Modulo que hace necesario estar logeado
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
def home_view(request):
    return render(request, 'hydroregis/home.html')

@login_required
def activities_view(request):
    return render(request, 'hydroregis/activities.html')

@login_required
def deposits_view(request):
    deposit_data = [
        {'name': 'Casa Arequipa', 'percentage': 45, 'liters': 1200},
        # Agrega más depósitos aquí
    ]
    return render(request, 'hydroregis/deposits.html', {'deposit_data': deposit_data})

def exit(request):
    logout(request)
    return redirect('home')
