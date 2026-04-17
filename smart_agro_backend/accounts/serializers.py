from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['username','mobile','email','password']

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            mobile=validated_data.get('mobile'),
            email=validated_data.get('email',''),
            password=validated_data['password']
        )


class LoginSerializer(serializers.Serializer):
    mobile_or_email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):

        value = data.get("mobile_or_email")
        password = data.get("password")

        user = None

        # check email
        if "@" in value:
            user = User.objects.filter(email=value).first()

        # check mobile
        if user is None:
            user = User.objects.filter(mobile=value).first()

        # check username
        if user is None:
            user = User.objects.filter(username=value).first()

        if user and user.check_password(password):
            data["user"] = user
            return data

        raise serializers.ValidationError("Invalid credentials")
