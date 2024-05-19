from django.shortcuts import render
from django.template import context
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data
from .serializers import DataSerializer


def welcome(request):
    # can add context information
    return render(request, "welcome.html")


@api_view(['GET'])
def get_data(request):
    app = Data.objects.all()
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post_data(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
