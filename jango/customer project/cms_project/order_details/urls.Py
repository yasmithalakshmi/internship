from django.urls import path
from order_details import views
urlpatterns = [
    path('', views.home ,name='home'),
]
