
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from watchlist_app.models import Watchlist, StreamPlatform, Review
from watchlist_app.api.serializers import WatchlistSerializer, StreamPlatformSerializer, ReviewSerializer
from watchlist_app.api.permissions import IsAdminOrReadOnly, IsReviewUser

class CreateReview(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = Watchlist.objects.get(pk=pk)
        
        review_user = self.request.user
        review_querset = Review.objects.filter(watchlist=watchlist, review_user=review_user)
        
        if review_querset.exists():
            raise ValidationError("You already reviewed")
        
        serializer.save(watchlist=watchlist, review_user=review_user)

class ReviewList(generics.ListAPIView):
    
    
    
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Review.objects.filter(watchlist=pk)
    

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    
    permission_classes = [IsReviewUser]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



class PlatformList(generics.ListCreateAPIView):
    
    permission_classes = [IsAdminOrReadOnly]
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

class StreamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer




# class PlatformList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
    
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class StreamDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class WatchlistAV(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        watchlist = Watchlist.objects.all()
        serializer = WatchlistSerializer(watchlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class WatchlistDetail(APIView):
    
    def get(self, request,pk):
        try:
            watchlist = Watchlist.objects.get(pk=pk)
        except:
            data = {'details':'No data found'}
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        serializer = WatchlistSerializer(watchlist)
        return Response(serializer.data)
    
    def put(self, request,pk):
        try:
            watchlist = Watchlist.objects.get(pk=pk)
        except:
            data = {'details':'No data found'}
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        
        serializer = WatchlistSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        try:
            watchlist = Watchlist.objects.get(pk=pk)
        except:
            data = {'details':'No data found'}
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        watchlist.delete()
        return Response({"detail":"Deleted succussfully"})
    

# @api_view(['GET','POST'])
# def watchlist(request):
#     if request.method == 'GET':
#         watchlist = Watchlist.objects.all()
#         serializer = WatchlistSerializer(watchlist, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = WatchlistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
        
# @api_view(['GET','PUT','DElEtE'])
# def watchlistDetail(request, pk):
    
#     if request.method == 'GET':
#         try:
#             watchlist = Watchlist.objects.get(pk=pk)
#         except:
#             data = {'details':'No data found'}
#             return Response(data, status=status.HTTP_204_NO_CONTENT)
#         serializer = WatchlistSerializer(watchlist)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         try:
#             watchlist = Watchlist.objects.get(pk=pk)
#         except:
#             data = {'details':'No data found'}
#             return Response(data, status=status.HTTP_204_NO_CONTENT)
        
#         serializer = WatchlistSerializer(watchlist, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     if request.method == 'DELETE':
#         try:
#             watchlist = Watchlist.objects.get(pk=pk)
#         except:
#             data = {'details':'No data found'}
#             return Response(data, status=status.HTTP_204_NO_CONTENT)
#         watchlist.delete()
#         return Response({"detail":"Deleted succussfully"})
    