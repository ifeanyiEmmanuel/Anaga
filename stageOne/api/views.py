from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


# Create your views here.
@api_view(['GET'])
def index(request):
    informations={
        "slackUsername":"Anaga", "backend": True,"age": 26, "bio": "am a python programmer,i build web applications using python and its frameworks,am a software Engineer "
    }
    return Response(informations)
