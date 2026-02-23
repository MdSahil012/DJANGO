"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('Login/',views.Login,name='Login'),
    path('Register/',views.Register,name='Register'),
    path('userdashboard/',views.userdashboard,name='userdashboard'),
    path('Logout/',views.Logout,name='Logout'),
    path('about/',views.about,name='about'),
    path('admindashboard/',views.admindashboard,name='admindashboard'),
    path('admindashboard/add_dep/',views.add_dep,name='add_dep'),
    path('admindashboard/show_dep/',views.show_dep,name='show_dep'),
    path('admindashboard/save_dep/',views.save_dep,name='save_dep'),
    path('admindashboard/add_emp/',views.add_emp,name='add_emp'),
    path('admindashboard/save_emp/',views.save_emp,name='save_emp'),
    path('admindashboard/show_emp/',views.show_emp,name='show_emp'),
    path('empdashboard/',views.empdashboard,name='empdashboard'),
    path('empdashboard/Profile/',views.Profile,name='Profile'),






]
