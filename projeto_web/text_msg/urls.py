from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('AreaLogada/', area_logada),
]
