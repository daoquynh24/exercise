# Python imports

# Django imports
from django.conf.urls import url

# Views imports
from .views import ListAllUserAPIView


urlpatterns = [
    url(r'^$', ListAllUserAPIView.as_view(), name='admin-list-all-user'),
]