from rest_framework import serializers
from .models import UserInfo

class UserInfoSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    other_names = serializers.CharField(required=False, allow_blank=True)
    d_o_b = serializers.DateField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()
    height = serializers.FloatField()
    weight = serializers.FloatField()
    jersey_size = serializers.CharField()
    shoe_size = serializers.CharField()
    passport_picture = serializers.ImageField()
    full_picture = serializers.ImageField()

    class Meta:
        model = UserInfo
        fields = '__all__'