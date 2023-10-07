<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculadora de IMC</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            text-align: center;
        }
        
        .calculator {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
            width: 300px;
            margin: 0 auto;
            padding: 20px;
        }

        h1 {
            color: #333;
        }

        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        button {
            background-color: #4CAF50;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #45a049;
        }

        #result {
            font-weight: bold;
            color: #333;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="calculator">
        <h1>Calculadora de IMC</h1>
        <input type="text" id="weight" placeholder="Peso (kg)">
        <input type="text" id="height" placeholder="Altura (m)">
        <button onclick="calculateIMC()">Calcular IMC</button>
        <div id="result"></div>
    </div>

    <script>
        function calculateIMC() {
            var weight = parseFloat(document.getElementById('weight').value);
            var height = parseFloat(document.getElementById('height').value);

            if (!isNaN(weight) && !isNaN(height) && height > 0) {
                var imc = weight / (height * height);
                var result = "";

                if (imc < 18.5) {
                    result = "Abaixo do peso";
                } else if (imc < 24.9) {
                    result = "Peso normal";
                } else if (imc < 29.9) {
                    result = "Sobrepeso";
                } else if (imc < 34.9) {
                    result = "Obesidade grau 1";
                } else if (imc < 39.9) {
                    result = "Obesidade grau 2";
                } else {
                    result = "Obesidade grau 3";
                }

                document.getElementById('result').innerHTML = "Seu IMC é: " + imc.toFixed(2) + "<br>Classificação: " + result;
            } else {
                document.getElementById('result').innerHTML = "Por favor, insira um peso e altura válidos.";
            }
        }
    </script>
</body>
</html>
