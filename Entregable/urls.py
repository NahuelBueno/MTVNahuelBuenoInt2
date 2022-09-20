from django.contrib import admin
from django.urls import path
from AppEntregable.views import familia


urlpatterns = [
    path('familia/', familia),
]