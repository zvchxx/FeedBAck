from django.urls import path
from django.utils.translation import gettext_lazy as _

from feedback import views

app_name = 'feedback'

urlpatterns = [
    path('show-offer/', views.show_offers_views_page, name='show-offer'),
    path('show-problem/', views.show_problems_views_page, name='show-problem'),
    path('offer/', views.offer_page_view, name='offer'),
    path('problem/', views.problem_page_view, name='problem'),
]