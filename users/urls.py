from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/',views.user_login_page_view, name='login'),
    path('register/', views.user_register_page_view, name='register'),
    path('checkout/', views.product_checkout_page_view, name='checkout'),
    path('verify-email/<uidb64>/<token>/', views.verify_email, name='verify-email'),
]
