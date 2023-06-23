from django.urls import path
from . import views


app_name = 'core'

urlpatterns = [
    path('', views.index),
    path('about-us', views.about, name='about'),
    path('why/', views.why, name='why'),
]
