from django.urls import re_path
from testing import views
urlpatterns = [
    re_path(r'^api/cars/(?P<id>\d+)', views.edit),
    re_path(r'^api/cars/$',views.index),
]
