from django.urls import path
from . import views

urlpatterns = [
    path("", views.getData, name='getData'),
     path("add/", views.addData, name='addData'),
    path('update/<int:pk>/', views.updateData, name='updateData'),
    path('delete/<int:pk>/', views.deleteData, name='deleteData'),
]
