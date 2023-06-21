from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import index, about, why


urlpatterns = [
    path('', index, name='index'),
    path('about-us/', about, name='about'),
    path('why/', why, name='why'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
