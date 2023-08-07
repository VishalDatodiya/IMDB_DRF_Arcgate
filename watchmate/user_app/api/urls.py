
from django.urls import path

# by default django provide us obtain_auth_token
# it is login link so we can get login token

from rest_framework.authtoken.views import obtain_auth_token
from user_app.api.views import registration_view

urlpatterns = [
    path('login/', obtain_auth_token, name="login"),
    path('register/', registration_view, name="register"),
]
