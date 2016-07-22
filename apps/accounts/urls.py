from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.UserLoginView.as_view(), name='user-login'),
    url(r'^register$', views.UserRegisterView.as_view(), name='user-register'),
    url(r'^logout$', views.logoutView, name='logout'),
]