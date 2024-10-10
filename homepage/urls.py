from django.urls import path

from homepage import views

app_name = 'home'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('404/', views.five_page_view, name='404'),\
    path('profile/', views.profil_page_view, name='profile'),
]
