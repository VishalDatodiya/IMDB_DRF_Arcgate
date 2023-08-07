from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from user_app.api.serializers import RegistrationSerializer
# from user_app import models

@api_view(['POST'])
def registration_view(request):
    
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Restration successfully!"
            data['username'] = account.username
            data['email'] = account.email

            # I can use this so I don't need model for creating token
            token, created = Token.objects.get_or_create(user=account)
            data['token'] = token.key
            
            # Or I can use signals for creating token see the models.py or django-rest-framework documetation
            # token = Token.objects.get(user=account).key
            # data['token'] = token
            
        else:
            data = serializer.errors    
            
        return Response(data)
        