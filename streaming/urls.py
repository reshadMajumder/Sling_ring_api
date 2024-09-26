from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from streaming.views import view_streams
# from room.views import post_ad,list_ads,ad_list_create,ad_detail

urlpatterns = [
    path('streams/', view_streams, name='login'),

]


