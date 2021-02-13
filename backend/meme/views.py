from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from .serializers import MemeSerializer     
from .models import Meme
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from django.core.exceptions import ObjectDoesNotExist


# view to handle get and post requests
@api_view(['GET', 'POST'])
def meme_list(request):

    # if request method is get then get all data and return 
    if request.method == 'GET':
        data = Meme.objects.all()
        serializer = MemeSerializer(data, context={'request': request},many=True)
        return Response(serializer.data)

    # if request method is post
    elif request.method == 'POST':
        serializer = MemeSerializer(data=request.data)

        #chcek if reuest is valid
        if serializer.is_valid():
            #check for duplicate post requests
            try:
                n = Meme.objects.get(name=request.data['name'],caption=request.data['caption'],url=request.data['url'])
                return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
            except ObjectDoesNotExist:
                serializer.save()
                return JsonResponse({'id':'{}'.format(serializer.data['id'])},status=status.HTTP_201_CREATED,safe=False)
        # else return error            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view to handle patch, delete, get requests
@api_view(['PATCH', 'DELETE','GET'])
def meme_detail(request, id):

   # check if meme with that id is present
   try:
        meme = Meme.objects.get(id=id)
   except Meme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
   
   #if request method is get then return data
   if request.method == 'GET':
        serializer = MemeSerializer(meme,context={'request': request})
        return Response(serializer.data)
   
   #if request method is patch then update meme with new data and return http status code
   elif request.method == 'PATCH':
        serializer = MemeSerializer(meme, data=request.data,context={'request': request},partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   # if request method is delete then delete meme
   elif request.method == 'DELETE':
        meme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 

