# Python imports

# Django imports
from django.conf.urls import url

# from users.admin.views import ListAllUserAPIView
# from users.views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView
from users.views import RegistrationAPIView

urlpatterns = [
    # url(r'^$', ListAllUserAPIView.as_view(), name='admin-list-all-user'),
    url(r'^users/?$', RegistrationAPIView.as_view()),
    # url(r'^users/login/?$', LoginAPIView.as_view()),
    # url(r'^user/', UserRetrieveUpdateAPIView.as_view()),

]


