from django.urls import path, include
from .views import *

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
]
