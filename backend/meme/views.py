from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import viewsets,generics          # add this
from .serializers import MemeSerializer      # add this
from .models import Meme

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import *

from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET', 'POST'])
def meme_list(request):
    if request.method == 'GET':
        data = Meme.objects.all()
        serializer = MemeSerializer(data, context={'request': request},many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MemeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                n = Meme.objects.get(name=request.data['name'],caption=request.data['caption'],url=request.data['url'])
                # m=Meme.objects.get(caption=request.data['caption'])
                # l==Meme.objects.get(url=request.data['url'])

                # number already exists
                return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
            except ObjectDoesNotExist:
                # number does not exist
                serializer.save()
                return JsonResponse({'id':'{}'.format(serializer.data['id'])},status=status.HTTP_201_CREATED,safe=False)
            # if ( request.data['name'] == request.data.pop('name') and
            #     request.data['caption'] == request.data.pop('caption') and
            #     request.data['url'] == request.data.pop('url')):
            #     return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
            # serializer.save()
            # return JsonResponse({'id':'{}'.format(serializer.data['id'])},status=status.HTTP_201_CREATED,safe=False)
            # return JsonResponse(serializer.data, status=status.HTTP_201_CREATED,safe=False)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH', 'DELETE','GET'])
def meme_detail(request, id):

   try:
        meme = Meme.objects.get(id=id)
   except Meme.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

   if request.method == 'GET':
        serializer = MemeSerializer(meme,context={'request': request})
        return Response(serializer.data)

   elif request.method == 'PATCH':
        serializer = MemeSerializer(meme, data=request.data,context={'request': request},partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
            # return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   elif request.method == 'DELETE':
        meme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # try:
    #     memes = Meme.objects.get(id=id)
    # except Meme.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
   
    # if request.method == 'GET':
    #     # data = memes
    #     serializer = MemeSerializer(memes, context={'request': request}, many=True)
    #     return Response(serializer.data)

    # elif request.method == 'PUT':
    #     serializer = MemeSerializer(memes, data=request.data,context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     memes.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def meme_list(request):
# #     """
# #  List  customers, or create a new customer.
# #  """
#    if request.method == 'GET':
#         data = []
#         nextPage = 1
#         previousPage = 1
#         customers = Meme.objects.all()
#         page = request.GET.get('page', 1)
#         paginator = Paginator(customers, 5)
#         try:
#             data = paginator.page(page)
#         except PageNotAnInteger:
#             data = paginator.page(1)
#         except EmptyPage:
#             data = paginator.page(paginator.num_pages)

#         serializer = MemeSerializer(data,context={'request': request} ,many=True)
#         if data.has_next():
#             nextPage = data.next_page_number()
#         if data.has_previous():
#             previousPage = data.previous_page_number()

#         return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/customers/?page=' + str(nextPage), 'prevlink': '/api/customers/?page=' + str(previousPage)})

#    elif request.method == 'POST':
#         serializer = MemeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

