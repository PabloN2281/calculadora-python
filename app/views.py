from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.

def calculator_view(request):
    resultado = None
    operacao = None

    if request.method == "POST":
        num1 = float(request.POST.get("num1"))
        num2 = float(request.POST.get("num2"))
        operacao = request.POST.get("operacao")

        if operacao == "adicionar":
            resultado = num1 + num2
        elif operacao == "subtrair":
            resultado = num1 - num2
        elif operacao == "multiplicar":
            resultado = num1 * num2
        elif operacao == "dividir":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Erro: Divisão por zero"
    os.system("git pull origin main")	
    return render(request, 'index.html', {'resultado': resultado, 'operacao': operacao})
def update(request):
    os.system("git pull origin main")
    return httpResponse("UPDATE")
