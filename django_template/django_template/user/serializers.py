from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)  
    email = serializers.EmailField(help_text="User's email address")
    name = serializers.CharField(help_text="User's full name")
    password = serializers.CharField(help_text="User's password", write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
