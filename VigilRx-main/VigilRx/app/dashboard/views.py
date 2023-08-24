from django.shortcuts import render


def home(request):
    return render(request, 'dashboard/home.html')

def base_view(request):
    return render(request, 'dashboard/base.html')