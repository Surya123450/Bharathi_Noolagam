from django.contrib import admin
from django.urls import path
from Bharathi_web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index),
    path('', views.index1),
    path('chapter/', views.chapter1,name='chapter'),
    path('about/', views.about,name='about'),
]
