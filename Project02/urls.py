"""Project02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from App02 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage,name='home'),
    path('admin1/',views.adminpage,name='admin1'),
    path('student/',views.studentpage,name='student'),
    path('adminpage/',views.adminhomepage,name='adminpage'),
    path('register/',views.register_page,name='register'),
    path('Studentlogin/',views.Student_login,name='Studentlogin')
]

