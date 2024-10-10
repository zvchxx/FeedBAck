from django.shortcuts import render

def home_page_view(request):
    return render(request, 'index.html')

def five_page_view(request):
    return render(request, 'main/404/404.html')

def profil_page_view(request):
    return render(request, 'main/profile/profile.html')