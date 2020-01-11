from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', views.product, name='product')
]