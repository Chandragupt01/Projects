from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class=MovieSerializer


class FeelGoodViewSet(viewsets.ModelViewSet):
    queryset=MovieData.objects.filter(genre='feelGood')
    serializer_class=MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset=MovieData.objects.filter(genre='Comedy')
    serializer_class=MovieSerializer
