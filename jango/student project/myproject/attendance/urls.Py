from student import views
from django.urls import path

urlpatterns = [
    path('', views.home, name ='home'),
    path('details/', views.details, name='details'),
]