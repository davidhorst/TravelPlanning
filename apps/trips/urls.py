from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name="home"),
    url(r'^add$', views.AddTripView.as_view(), name="add-trip"),
    url(r'^join/(?P<pk>[0-9]+)/$', views.jointrip, name="join-trip"),
    url(r'^destinations/(?P<pk>[0-9]+)/$', views.TripDetailView.as_view(), name="trip detail")
]
