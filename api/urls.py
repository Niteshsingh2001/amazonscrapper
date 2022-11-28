from django.urls import path
from .views import amazon_data

urlpatterns = [
    path("api/", amazon_data,name="amazon_data"),

]
