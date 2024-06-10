from django.shortcuts import render
from .models import *
from .serializers import *

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status  

class UsuarioCustomizadoView(ModelViewSet):
    queryset = UsuarioCustomizado.objects.all()
    serializer_class = UsuarioCustomizadoSerializer

class GeneroLivroView(ModelViewSet):
    queryset = GeneroLivro.objects.all()
    serializer_class = GeneroLivroSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']
    permission_classes = (IsAuthenticated,)
    

class LivrosView(ModelViewSet):
    queryset = Livros.objects.filter(aprovado='A')
    serializer_class = LivrosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['titulo', 'GeneroLivroFK']
    
class EmprestimoView(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    permission_classes = (IsAuthenticated,)

class EmprestimoLivrosView(ModelViewSet):
    queryset = EmprestimoLivros.objects.all()
    serializer_class = EmprestimoLivrosSerializer
    permission_classes = (IsAuthenticated,)

# teste