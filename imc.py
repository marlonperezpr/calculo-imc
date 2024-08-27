#Programa de calculo de IMC com Python

peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Magreza"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"
    
print("Seu IMC é: {:.2f}".format(imc))
print("Sua classificação é: {}".format(classificar_imc(imc)))
