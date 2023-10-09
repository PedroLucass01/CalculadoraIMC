
Passo 1: Configure um ambiente de desenvolvimento Django
Antes de criar a aplicação, certifique-se de ter o Django instalado. Você pode instalá-lo usando o pip:

bash
pip install django
Em seguida, crie um novo projeto Django e um aplicativo dentro do projeto:

bash
Copy code
django-admin startproject imc_project
cd imc_project
python manage.py startapp imc_calculator
Passo 2: Defina o modelo de dados
Em seu aplicativo imc_calculator, defina o modelo de dados para representar as informações necessárias para calcular o IMC. Abra o arquivo models.py em seu aplicativo e adicione o seguinte código:

python
Copy code
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
Em seguida, crie as migrações e aplique-as ao banco de dados:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Passo 3: Crie as visualizações
Agora, crie as visualizações para permitir que os usuários insiram dados e vejam os resultados do IMC. Abra o arquivo views.py em seu aplicativo e adicione o seguinte código:

python
Copy code
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
Passo 4: Crie os templates HTML
Crie os templates HTML para a entrada de dados e a exibição dos resultados. Crie uma pasta chamada templates em seu aplicativo e dentro dela crie dois arquivos: calcular_imc.html e resultado.html.

calcular_imc.html:

html
Copy code
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

html
Copy code
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
Passo 5: Configure as URLs
Em seu aplicativo, crie um arquivo urls.py e adicione o seguinte código:

python
Copy code
from django.urls import path
from . import views

urlpatterns = [
    path('', views.calcular_imc, name='calcular_imc'),
]
Passo 6: Configure as URLs do projeto principal
Em seu projeto principal, abra o arquivo urls.py e adicione o seguinte código para incluir as URLs do aplicativo imc_calculator:

python
Copy code
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('imc/', include('imc_calculator.urls')),
]
