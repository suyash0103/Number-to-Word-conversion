# import sys
# sys.path.append(".")

from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('identity', (views.Identity.as_view()), name='identity'),
    path('convert', (views.Convert.as_view()), name='convert'),

    # path('ch', views.check, name='check'),
]

