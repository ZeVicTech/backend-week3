from django.shortcuts import render
from .models import House
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import HouseSerializer


# Create your views here.

class Houses(APIView):
    def get(self, request):
        all_houses = House.objects.all()
        serializer = HouseSerializer(all_houses, many=True)
        return Response(serializer.data)


