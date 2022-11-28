from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from django.shortcuts import get_object_or_404 
from base.models import Item
from .serializers import ItemSerializer

# get all the data
@api_view(['GET'])
def getData(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Item.objects.filter(**request.query_params.dict())
    else:
        items = Item.objects.all()
  
    # if there is something in items else raise error
    if items:
        serializer = ItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

# for post a data
@api_view(['POST'])
def addData(request):
     item = ItemSerializer(data=request.data)
    # validating for already existing data
     if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
     if item.is_valid():
        item.save()
        return Response(item.data)
     else:
        return Response(status=status.HTTP_404_NOT_FOUND)

        # for update 
@api_view(['POST'])
def updateData(request, pk):
    item = Item.objects.get(pk=pk)
    data = ItemSerializer(instance=item, data=request.data, partial=True)
  
    if data.is_valid():
        data.save()
        return Response({"status": "success", "data": data.data})  
    else:
          return Response({"status": "error", "data": data.errors})  

# for delete

@api_view(['DELETE'])
def deleteData(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response({"status": "success", "data": "Record Deleted"})  