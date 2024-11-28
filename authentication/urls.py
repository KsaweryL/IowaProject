from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import log_in, log_out, register_user

urlpatterns = [
path('login/', log_in, name="login"),
path("logout/", log_out,name="logout"),
path("sign_up/", register_user, name = "sign_up")
]
