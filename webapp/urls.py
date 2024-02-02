from django.urls import path
from . import views
from .views import login_view


urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('techblog/', views.techblog, name="techblog"),
    path('services/', views.services, name="services"),
    path('crud/', views.crud, name="crud"),
    path('language/', views.language, name="language"),
    path('stacks/', views.stacks, name="stacks"),
    path('framework/', views.framework, name="framework"),
    path('ide/', views.ide, name="ide"),
    path('update_Laptop/<int:pk>/', views.updateLaptop, name="updateLaptop"),
    path('delete_laptop/<int:pk>/', views.deleteLaptop, name="deleteLaptop"),
    path ('create_laptop/', views.addForm, name="addForm"),
    path('login/', login_view, name='login'),


]