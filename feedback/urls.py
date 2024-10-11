from django.urls import path
from django.utils.translation import gettext_lazy as _

from feedback import views

app_name = 'feedback'

urlpatterns = [
    path('show/', views.show_offers_views_page, name='show'),
    path('offer/', views.offer_page_view, name='offer'),
    path('problem/', views.problem_page_view, name='problem'),
]
