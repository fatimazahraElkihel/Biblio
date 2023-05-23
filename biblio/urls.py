from django.urls import path
from .views import uneVue
from Gestion_book import views

urlpatterns = [
    path('page1/', uneVue, name='page_une'),
    path('', views.main)
]


