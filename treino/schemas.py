from ninja import ModelSchema
from .models import Alunos

class AlunoSchema(ModelSchema):
    class Meta:
        model = Alunos
        fields = ['nome', 'email', 'faixa', 'data_nascimento']