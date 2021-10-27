from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import CardSerializer
from .models import Card

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

@api_view(['GET'])
def cardList(request):
    cards = Card.objects.all()
    serializer = CardSerializer(cards, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def cardDetail(request,pk):
    card = Card.objects.get(id=pk)
    serializer = CardSerializer(card, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def cardCreate(request):
    serializer = CardSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def cardUpdate(request, pk):
    card = Card.objects.get(id=pk)
    serializer = CardSerializer(instance=card, data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)
