from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.index),
    path('<str:sender>/<str:password_app>/<str:recipient>/<str:subject>/<str:message>', views.send, name="index"),
]