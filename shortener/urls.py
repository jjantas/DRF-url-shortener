from django.urls import path
from .views import CreateShortURL

urlpatterns = [
    path('api/shorten/', CreateShortURL.as_view(), name='create-short-url'),
]