from django.urls import path
from .import views

urlpatterns = [
    path('addCaloToday/', views.AddCaloToday.as_view(), name='nameAddCaloToday'),
]
