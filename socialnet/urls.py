"""
URL configuration for socialnet project.

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
from core.views import *
from core.views import about_us
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('contacts/', contacts),
    path('about_us/', about_us),
    path('posts/<int:id>', post_detail),
    path('profile/<int:id>', post_detail, name='profile'),
    # path('shorts/', shorts_list, name='shorts_list'),
    path('shorts/<int:id>/', shorts_detail, name='shorts_detail'),
    # path('category/', category_list, name='category_list'),
    path('category/<int:id>/', category_detail, name='category_detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)