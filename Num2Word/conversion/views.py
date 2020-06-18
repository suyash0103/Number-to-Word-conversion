from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.

def getResponse(request):
    GETResponse = {
        'server_name': 'Suyash Ghuge'
    }
    return JsonResponse(GETResponse)

def postResponse(request):
    number = request.POST.get('value')
    POSTResponse = {
        'server_name': number
    }
    return JsonResponse(POSTResponse)


# def check(request):
#     return HttpResponse("checked")