from django.urls import path
from . import views

urlpatterns = [
    #path (url_pattern, function, name(optional))
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("cats/", views.cats_index, name="index"),

]