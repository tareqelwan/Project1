from django.urls import path

from .views import (
    # main menu
    landing_page,    
    )

app_name = 'sales'

urlpatterns = [
    path('',landing_page),      
]
