from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [

]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('homepage.urls', namespace="home")),
    path('feedback/', include('feedback.urls', namespace="feedback")),
    path('users/', include('users.urls', namespace="users")),
    path('comment/', include('comment.urls', namespace="comment")),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)