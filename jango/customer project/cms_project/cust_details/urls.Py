from django.urls import path
from cust_details import views
urlpatterns = [
    path('', views.home ,name='home'),
]
