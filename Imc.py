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
