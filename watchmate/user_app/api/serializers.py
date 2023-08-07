from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError

class RegistrationSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField( style={'input_type':'password'} ,write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise ValidationError("P1 and P2 are same")
        
        user_queryset = User.objects.filter(email=self.validated_data['email'])
        if user_queryset.exists():
            raise ValidationError("Email already exist")
        
        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account