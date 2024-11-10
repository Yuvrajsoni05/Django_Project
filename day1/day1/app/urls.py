from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('insertdata', views.inserdata, name='insertdata'),
    path('deletedata/<int:pk>/', views.data_delete, name='deletedata'),  # Added trailing slash
    path('updatepage/<int:pk>/', views.updatePage, name='updatePage'),
    path('updatedata/<int:pk>/', views.updateData, name='updateData'),

]
