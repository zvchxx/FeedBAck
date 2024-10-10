from django.urls import path
from django.utils.translation import gettext_lazy as _

from feedback.views import show_offer_problem_page_view, offer_problem_page_view

app_name = 'feedback'

urlpatterns = [
    path('show/', show_offer_problem_page_view, name='show'),
    path('write/', offer_problem_page_view, name='write'),
]
