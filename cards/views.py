from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/card-list/',
        'Detail View':'/card-detail/<str:pk>/', 
        'Create':'/card-create/',
        'Update':'/card-update/<str:pk>/',
    }

    return Response(api_urls)