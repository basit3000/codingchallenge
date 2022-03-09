from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('result/offer/<str:pk>/',views.resultOffer, name="offer"),
    path('result/event/<str:pk>/',views.resultEvent, name="event"),
]