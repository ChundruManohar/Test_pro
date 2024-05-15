from django.shortcuts import render
from rest_framework.decorators import api_view  
from rest_framework.response import Response
from rest_framework import status
from. import models
from .main import KeyValueSerializer

# Create your views here.


@api_view(['GET'])  
def home(request):
    return Response("Welcome to the Address Book API")  

@api_view(['GET'])
def get_all_addresses(request):
    addresses = models.Address.objects.all()
    serializer = KeyValueSerializer(addresses, many=True)
    return Response({"message":serializer.data,"status":"success"})

@api_view(['POST']) 
def create(request):
    adresses = models.Address.objects.all()
    serializer = KeyValueSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])  
def update(request, id):
    address = models.Address.objects.get(id=id)
    serializer = KeyValueSerializer(instance=address, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Address updated successfully"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_user(request, id):
    address = models.Address.objects.get(id=id)
    address.delete()
    return Response({"message":"Address deleted successfully"}, status=status.HTTP_200_OK)

