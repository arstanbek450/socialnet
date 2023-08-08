from django.contrib import admin
from django.urls import path
from core.views import *
from django.conf import settings # !
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('posts/<int:id>', post_detail),
    path('profile/<int:id>', profile_detail, name='profile'),
    path('shorts/', shorts, name='shorts_list'),
    path('shorts/<int:id>/', short_info, name='shorts_detail'),
    path('categories/', category_list, name='category_list'),
    path('categories/<int:id>/', category_detail, name='category-detail'),
    path('saved_posts/', saved_posts_list, name='saved-posts'),
    path('<int:user_id>/', user_posts, name='user-posts'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




