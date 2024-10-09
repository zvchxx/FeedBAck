from django.urls import path

from homepage import views

app_name = 'home'

urlpatterns = [
    path('', views.home_page_view, name='home'),
]
