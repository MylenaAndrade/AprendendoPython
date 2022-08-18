#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
#Armazene os números pares no vetor PAR e os números IMPARES no vetor 
#impar. Imprima os três vetores.
vetor = []
vetorPar = []
vetorImpar = []

for i in range(0,20):
    numero=int(input("Escolha um número: "))
    vetor[i] = numero
    if vetor[i] % 2 == 0:
        vetorPar[j]=vetor[i]
        j += 1
    else:
        vetorImpar[k]=vetor[i]
print("Vetor Original: ", vetor)
print("Vetor Par: ", vetorPar)
print("Vetor Impar: ", vetorImpar)
