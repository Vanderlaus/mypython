from django.shortcuts import render
from .models import Alunos


# Create your views here.
def index(request):
    alunos = Alunos.objects.all()
    dados = {
        'alunos' : alunos
    }
    
    return render(request, 'index.html', dados)
  

def aluno(request):
    return render(request,'aluno.html')

# Create your views here.
