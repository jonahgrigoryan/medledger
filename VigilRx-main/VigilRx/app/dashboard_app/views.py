from django.shortcuts import render


def home(request):
    print("home view triggered")
    context = {
        'title': 'Dashboardd'
    }
    return render(request, 'dashboard_app/home.html', context)

def base_view(request):
    return render(request, 'dashboard_app/base.html')