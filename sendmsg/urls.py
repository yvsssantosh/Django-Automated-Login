from django.conf.urls import url, include

from .views import user_logged_in

urlpatterns = [
    url(r'^$', user_logged_in, name="user_logged_in"),
]
