from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from authentication.views import login_view,logout_view,register_view
# from room.views import post_ad,list_ads,ad_list_create,ad_detail

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]


