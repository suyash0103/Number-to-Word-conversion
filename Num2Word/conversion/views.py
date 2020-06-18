from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class Identity(APIView):

    def get(self, request):
        GETResponse = {
            'server_name': 'Suyash Ghuge'
        }
        return Response(GETResponse, status=status.HTTP_200_OK)

    

class Convert(APIView):

    def post(self, request):
        val = request.data['value']
        GETResponse = {
            'server_name': val
        }
        val = int(val)
        if val < 0:
            content = {"Value should be greater than 0"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        return Response(GETResponse, status=status.HTTP_200_OK)
     