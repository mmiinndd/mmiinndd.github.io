from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.base.as_view()),
    path('', views.raffle.as_view()),
]
