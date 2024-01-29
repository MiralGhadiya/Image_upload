from rest_framework import serializers
from .models import *


class Blogserializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields='__all__'

class EmailSerializer(serializers.Serializer):
    class Meta:
        model=EmailData
        fields=['firstname', 'lastname','subject', 'message','email']
        
    def create(self, validated_data):
        return EmailData.objects.create(**validated_data)
    