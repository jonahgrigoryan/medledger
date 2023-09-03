from django.shortcuts import render


def home(request):
    return render(request, 'dashboard_app/home.html')

def base_view(request):
    return render(request, 'dashboard_app/base.html')