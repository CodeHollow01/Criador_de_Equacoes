import random
import re

def operação():
    valores = [ #Cria os valores numéricos usados para a equação
    random.randrange(0,9),
    random.randrange(0,9),
    random.randrange(0,9),
    random.randrange(0,9)
    ]

    global resposta_real #Faz a variável poder ser usada fora da função
    resposta_real = 1
    operador = random.randrange(1,5) #Seleciona a ordem dos operadores

    if operador == 1:
        resposta_real = valores[0] * valores[1] + valores[2] - valores[3] #Obtem o resultado da equação criada
        resposta_input = input("Qual é o resultado da expressão? " + str(valores[0]) + " * " + str(valores[1]) + " + " + str(valores[2]) + " - " + str(valores[3]) + ": ")
        resposta_input = re.sub("[^0-9-]","91",resposta_input) #Faz com que toda a resposta que não contenha numeros de 0-9 ou - seja invalidada
        if resposta_real == int(resposta_input): #Compara as respostas
            return True
        else:
            return False

    elif operador == 2: #Repetindo o padrão para o resto dos operadores usando elif para caso um deles forem verdadeiros, pule os outros para deixar melhor otimizado
            resposta_real = valores[0] + valores[1] - valores[2] * valores[3]
            resposta_input = input("Qual é o resultado da expressão? " + str(valores[0]) + " + " + str(valores[1]) + " - " + str(valores[2]) + " * " + str(valores[3]) + ": ")
            resposta_input = re.sub("[^0-9-]","91",resposta_input)
            if resposta_real == int(resposta_input):
                return True
            else:
                return False
                
                   
    elif operador == 3:
            resposta_real = valores[0] - valores[1] * valores[2] + valores[3]
            resposta_input = input("Qual é o resultado da expressão? " + str(valores[0]) + " - " + str(valores[1]) +  " * " + str(valores[2]) + " + " + str(valores[3]) + ": ")
            resposta_input = re.sub("[^0-9-]","91",resposta_input)
            if resposta_real == int(resposta_input):
                return True
            else:
                return False
    
    else:
            resposta_real = valores[0] * valores[1] - valores[2] + valores[3]
            resposta_input = input("Qual é o resultado da expressão? " + str(valores[0]) + " * " + str(valores[1]) + " - " + str(valores[2]) + " + " + str(valores[3]) + ": ")
            resposta_input = re.sub("[^0-9-]","91",resposta_input)
            if resposta_real == int(resposta_input):
                return True
            else:
                return False

if operação(): #Se a função "operação" retornar True 
    print("Certa resposta!")
else: #Se a função "operação" retornar False
    print("Errou!")
    print("Resposta certa: " + str(resposta_real))