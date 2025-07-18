from django.contrib import admin
from django.urls import path
from Myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('browse/', views.browse, name='browse'),
    path('details/', views.details, name='details'),
    path('profile/', views.profile, name='profile'),
    path('streams/', views.streams, name='streams'),
]
