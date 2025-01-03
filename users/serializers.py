from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError
from django.contrib.auth import get_user_model
from .models import User


User = get_user_model()

# This code is a combination of two contributors, me and Jonathan(jod35)


class SignUpSerializer(serializers.ModelSerializer):
    """
    This will serialize the data provided by the user.
    """

    email = serializers.CharField(max_length=80)

    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password"]

        extra_kwargs = {
            'password': {'write_only': True},  
            'email': {'required': True},  
          }
        

    def validate_email(self, value):

        if not value:
            raise serializers.ValidationError("Email is required.")
        if '@' not in value:
            raise serializers.ValidationError("Enter a valid email address.")
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email has already been used")
        return value
       
        
       

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

       
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class CurrentUserPostsSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True, view_name="post_detail", queryset=User.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "email", "posts"]
