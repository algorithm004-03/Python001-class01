from django.urls import path
from . import views
urlpatterns = [
    path('movies/', views.movies),
    path('', views.login2),
    path('form/', views.form1),
    path('login2', views.login2)
]
