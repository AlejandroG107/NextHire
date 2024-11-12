from .models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')

    #Validar que ambas contraseñas coincidan
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('Las contraseñas no coinciden')
        return attrs

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_staff=validated_data.get['is_staff', False],
            is_superuser=validated_data.get['is_superuser', False]
        )
        user.set_password(validated_data['password']) #Encriptar la contraseña
        user.save()
        return user