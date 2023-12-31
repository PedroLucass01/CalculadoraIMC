 models.py
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    altura = models.DecimalField(max_digits=5, decimal_places=2)

    def calcular_imc(self):
        altura_metros = self.altura / 100  # Convertendo altura de cm para metros
        return self.peso / (altura_metros ** 2)

    def classificar_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 25:
            return "Peso normal"
        elif 25 <= imc < 30:
            return "Acima do peso"
        else:
            return "Obesidade"

    def __str__(self):
        return self.nome

    Views.py 
from django.shortcuts import render
from .models import Pessoa

def calcular_imc(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        peso = float(request.POST['peso'])
        altura = float(request.POST['altura'])

        pessoa = Pessoa(nome=nome, peso=peso, altura=altura)
        pessoa.save()
        classificacao = pessoa.classificar_imc()
        return render(request, 'resultado.html', {'pessoa': pessoa, 'classificacao': classificacao})
    return render(request, 'calcular_imc.html')
  
 Criar templates em html 
calcular_imc.html

<!DOCTYPE html>
<html>
<head>
    <title>Calculadora de IMC</title>
</head>
<body>
    <h1>Calculadora de IMC</h1>
    <form method="post">
        {% csrf_token %}
        <label for="nome">Nome:</label>
        <input type="text" name="nome" required><br>
        <label for="peso">Peso (kg):</label>
        <input type="number" name="peso" step="0.01" required><br>
        <label for="altura">Altura (cm):</label>
        <input type="number" name="altura" step="0.01" required><br>
        <input type="submit" value="Calcular">
    </form>
</body>
</html>


resultado.html:

<!DOCTYPE html>
<html>
<head>
    <title>Resultado do IMC</title>
</head>
<body>
    <h1>Resultado do IMC</h1>
    <p>Nome: {{ pessoa.nome }}</p>
    <p>Peso: {{ pessoa.peso }} kg</p>
    <p>Altura: {{ pessoa.altura }} cm</p>
    <p>IMC: {{ pessoa.calcular_imc }}</p>
    <p>Classificação: {{ classificacao }}</p>
    <a href="{% url 'calcular_imc' %}">Calcular novamente</a>
</body>
</html>

url.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.calcular_imc, name='calcular_imc'),
]


Em seu projeto principal, abra o arquivo urls.py e adicione o seguinte código para incluir as URLs do aplicativo imc_calculator:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('imc/', include('imc_calculator.urls')),
]
