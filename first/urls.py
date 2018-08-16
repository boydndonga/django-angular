from django.urls import path
from first import views

urlpatterns = [
    path(r'^$', views.HomePageView.as_view()),
    path(r'^links/$', views.LinksPageView.as_view())
]