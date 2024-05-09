
from django.urls import path
from . import views

url_patterns = [
    # path('', views.api_root)
    path('', views.get_data),
    path('add/', views.add_item)
]