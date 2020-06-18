# import sys
# sys.path.append(".")

from django.urls import path
from . import views

urlpatterns = [
    path('identity', views.getResponse, name='getResponse'),
    path('convert', views.postResponse, name='postResponse'),

    # path('ch', views.check, name='check'),
]

