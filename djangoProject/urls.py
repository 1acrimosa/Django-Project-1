from django.contrib import admin
from django.urls import path
from core.views import index, about, why


urlpatterns = [
    path('', index, name='index'),
    path('about-us/', about, name='about'),
    path('why/', why, name='why'),
    path('admin/', admin.site.urls),
]
