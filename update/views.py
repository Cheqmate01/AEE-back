from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Update
from .serializers import UpdateSerializer

# Create your views here.
class LatestUpdatesView(APIView):
    def get(self, request):
        updates = Update.objects.order_by('-event_date', '-id')[:3]
        serializer = UpdateSerializer(updates, many=True, context={'request': request})
        return Response(serializer.data)