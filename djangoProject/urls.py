from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import about, why


urlpatterns = [
    path('', include('core.urls')),
    path('about-us/', about, name='about'),
    path('why/', why, name='why'),
    path('items/', include('item.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)