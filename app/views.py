from django.shortcuts import render

# Create your views here.

def calculator_view(request):
    resultado = None
    operacao = None

    if request.method == "POST":
        numero1 = float(request.POST.get("num1"))
        numero2 = float(request.POST.get("num2"))
        operacao = request.POST.get("operacao")

        if operacao == "adicionar":
            resultado = numero1 + numero2
        elif operacao == "subtrair":
            resultado = numero1 - numero2
        elif operacao == "multiplicar":
            resultado = numero1 * numero2
        elif operacao == "dividir":
            if num2 != 0:
                resultado = numero1 / numero2
            else:
                resultado = "Erro: Divisão por zero"

    return render(request, 'index.html', {'resultado': resultado, 'operacao': operacao})
