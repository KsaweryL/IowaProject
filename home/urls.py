from django.urls import path
from .views import home_page, test_page
urlpatterns = [
    path('', home_page, name='home-page'),
    path('test/', test_page, name='test-page'),
]