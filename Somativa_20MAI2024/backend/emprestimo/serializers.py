from rest_framework import serializers
from .models import *

class UsuarioCustomizadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioCustomizado
        fields = ['id','email','telefone','cpf','endereco','is_active','groups','user_permissions']
        many = True

class GeneroLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneroLivro
        fields = '__all__'
        many = True

class FotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        fields = '__all__'
        many = True

class LivrosSerializer(serializers.ModelSerializer):
    fotoFK = FotoSerializer(read_only=True)
    GeneroLivroFK = GeneroLivroSerializer(read_only=True)
    class Meta:
        model = Livros
        fields = '__all__'
        many = True

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'
        many = True

class EmprestimoLivrosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmprestimoLivros
        fields = '__all__'

        
