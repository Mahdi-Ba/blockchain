from django.urls import path
from .api import views


urlpatterns = [
    path('address/info', views.AddressInfo.as_view(), name=None),
]
