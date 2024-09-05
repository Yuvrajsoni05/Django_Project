from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('add_todo',views.add_todo,name="add_todo"),
    path('user_login/', views.user_login, name="user_login"),
    path('signup/', views.signup, name="signup"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('change-status/<int:id>/<str:status>/', views.change_status, name='change-status'),




]
