from django.urls import path, include
from calculator import views

urlpatterns = [
    path('tablecalo/', views.tableCalo, name='nameTableCalo'),
    path('cal/', views.calculateCalorites, name='nameCalculateCalories'),
    path('getjson', views.getJson, name='nameGetJson'),
    path('caloperday/', views.caloCaloPerDay, name='nameCaloPerDay'),
]