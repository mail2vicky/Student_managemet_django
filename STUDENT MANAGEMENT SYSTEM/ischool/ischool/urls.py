"""
URL configuration for ischool project.

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
from home.views import *

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('login_page',login_page,name='login_page'),
    path('logout_page',logout_page,name='logout_page'),
    path('home',home,name='home'),
    path('dashboard',dashboard,name='dashboard'),
    
    path('delete_student/<id>',delete_student,name="delete_student"),
    path('update_student/<id>',update_student,name="update_student"),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        
urlpatterns += staticfiles_urlpatterns()


admin.site.site_header = "Admin "
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Admin Researcher Portal"