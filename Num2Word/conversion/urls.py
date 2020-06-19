# import sys
# sys.path.append(".")

from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # URL for /identity
    path('identity', (views.Identity.as_view()), name='identity'),

    #URL for /convert
    path('convert', (views.Convert.as_view()), name='convert'),
]

