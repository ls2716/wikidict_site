from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    # path pattern to the basic view
    path('', views.home, name='home'),
    path('info/', views.info, name='info'),
    path('contact/', views.contact, name='contact'),
    path('query/<str:query>/', views.query, name='query'),
]