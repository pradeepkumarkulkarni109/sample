from rest_framework import serializers
from register.models import Signup

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ('id', 'full_name', 'email', 'phone_number', 'password')
