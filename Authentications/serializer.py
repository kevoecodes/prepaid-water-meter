from dataclasses import fields

from rest_framework import serializers
from .models import NewUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('mobileNo', 'first_name', 'last_name', 'accountNo', 'deviceNo')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('mobileNo', 'password')

""" class CrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cr
        fields = ('username', 'password', 'department', 'programme', 'year', 'classNo' ) """