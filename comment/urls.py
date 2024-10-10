from django.urls import path
from django.utils.translation import gettext_lazy as _

from comment.views import comment_problem_page_view

app_name = 'comment'

urlpatterns = [
    path('comment/', comment_problem_page_view, name='comment'),
]
