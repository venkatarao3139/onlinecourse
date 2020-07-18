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
    # ================Admin and Course urls====================================
    path('',views.homepage,name='home'),
    path('admin1/',views.adminpage,name='admin1'),
    path('adminpage/',views.adminhomepage,name='adminpage'),
    path('newcource/',views.newcource,name='newcource'),
    path('svaecourse/',views.svaecourse,name='svaecourse'),
    path('courseslist/',views.courseslist,name='courseslist'),
    path('updatet<int:pk>/',views.Updatecourse.as_view(),name='update'),
    path('remove<int:pk>/',views.Remove_course.as_view(),name='remove'),
    # ================student urls=============================================
    path('student/', views.studentpage, name='student'),
    path('Studentlogin/', views.Student_login, name='Studentlogin'),
    path('register/',views.register_page,name='register'),
    path('savestdent/', views.savestdent, name='savestdent'),
    path('studentloginhome/',views.studentlogin_home,name='studentloginhome'),
    path('student_home/', views.student_home, name='student_home'),
    path('students_list/',views.student_list ,name='students_list')





]

