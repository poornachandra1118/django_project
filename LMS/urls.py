"""
URL configuration for LMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app1.views import *

from  django.conf.urls.static import static
from LMS import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Dashboard',Dashboard,name='Dashboard'),
    path('Course_details/<str:pk>',Course_details,name='Course_details'),
    path('Profile',Profile,name='Profile'),
    path('Create_student',Create_student,name='Create_student'),
    path('Videos_allocation',Videos_allocation,name='Videos_allocation'),
    path('Course_allocation',Course_allocation,name='Course_allocation'),
    path('Student_details',Student_data,name='Student_details'),
    
    path('Student_login',Student_login,name='Student_login'),
    path('Admin_login',Admin_login,name='Admin_login'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

