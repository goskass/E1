from django.contrib import admin
from django.urls import path
from hobby_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('admin/', admin.site.urls),
]