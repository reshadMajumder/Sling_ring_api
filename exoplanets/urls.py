from django.urls import path
from .views import get_exoplanet_data

urlpatterns = [
    path('exoplanets/', get_exoplanet_data, name='fetch_exoplanet_data'),
]
