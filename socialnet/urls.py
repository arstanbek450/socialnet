from django.contrib import admin
from django.urls import path, include
from core.views import *
from django.conf import settings # !
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('posts/<int:id>/', post_detail),
    path('profile/<int:id>/', profile_detail, name='profile'),
    path('shorts/', shorts, name='shorts-list'),
    path('short/<int:id>/', short_info, name='shorts-info'),
    path('saved_posts/', saved_posts_list, name='saved-posts'),
    path('<int:user_id>/', user_posts, name='user-posts'),
    path('add-post/', create_post, name='add-post'),
    path('add-short/', add_short, name='add-short'),
    path('add-saved/', add_saved, name='add-saved'),
    path('users/', include('userapp.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



