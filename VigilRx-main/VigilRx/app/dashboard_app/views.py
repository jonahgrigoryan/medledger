from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    print("home view triggered")
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard_app/home.html', context)

def base_view(request):
    return render(request, 'dashboard_app/base.html')