from django.urls import path
from . import views
from .views import delete_view

urlpatterns = [
    path('', views.home, name="home"),
    path('create/', views.create, name="create"),
    path('<id>/delete', delete_view , name="delete"),
    path('update/<int:id>/', views.update, name="update"),
]