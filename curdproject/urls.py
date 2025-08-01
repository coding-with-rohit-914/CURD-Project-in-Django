"""
URL configuration for curdproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from curdapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexPage),
    path('indexPage', views.indexPage, name='indexPage'),
    path('add_student', views.add_student, name='add_student'),
    path('update_student/<id>', views.update_student, name='update_student'),
    path('updated_data/<id>', views.updated_data, name='updated_data'),
    path('delete_student/<id>', views.delete_student, name='delete_student')
]
