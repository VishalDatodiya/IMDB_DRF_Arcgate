
from rest_framework import serializers
# from rest_framework.validators import ValidationError

from watchlist_app.models import Watchlist, StreamPlatform, Review



class ReviewSerializer(serializers.ModelSerializer):
    
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = '__all__'


class WatchlistSerializer(serializers.ModelSerializer):
    
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Watchlist
        fields = '__all__'
        
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    
    watclist = WatchlistSerializer(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        
        
        
        

# class WatchlistSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     storyline = serializers.CharField()
#     active = serializers.BooleanField()
#     updated = serializers.DateTimeField()
#     created = serializers.DateTimeField()
    
    
#     def create(self, validated_data):
#         return Watchlist.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.storyline = validated_data.get('storyline', instance.storyline)
#         instance.active = validated_data.get('active', instance.active)
#         instance.updated = validated_data.get('updated', instance.updated)
#         instance.created = validated_data.get('created', instance.created)
        
#         instance.save()
#         return instance
    
    
    # def validate_title(self,value):
    #     if len(value) > 2:
    #         return value
    #     raise ValidationError("Name is too short!")
    
    # def validate(self, attrs):
    #     return super().validate(attrs)
    