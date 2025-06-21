from django.urls import path
from .views import CreateShortURL, RedirectShortURL

urlpatterns = [
    path('api/shorten/', CreateShortURL.as_view(), name='create-short-url'),
    path('shrt/<str:code>/', RedirectShortURL.as_view(), name='redirect-short-url'),
]