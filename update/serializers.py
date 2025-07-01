# update/serializers.py
from rest_framework import serializers
from .models import Update

class UpdateSerializer(serializers.ModelSerializer):
    event_picture = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Update
        fields = '__all__'