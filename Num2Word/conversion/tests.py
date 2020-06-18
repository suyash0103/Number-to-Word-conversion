import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
from rest_framework.test import APIRequestFactory
# settings.configure()

# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.post('/convert/', {'value': 1})


# client = Client()