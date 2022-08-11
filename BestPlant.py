#Escreve um programa que utilize o conceito de execução condicional, toma uma string como entrada, e:
#    *imprime a frase "Yes - Spathiphyllum is the best plant ever!" para o ecrã, se 
#    a cadeia de caracteres inseridos é "Spathiphyllum" (upper-case)
#    *Impressões "No, I want a big Spathiphyllum!" se a cadeia de caracteres inseridos 
#    é "spathiphyllum" (lower-case)
#    *Impressões "Spathiphyllum! Not [input]!" 
#    caso contrário. Nota: [input] é a string tomada como input.

plant=input("Which is the best plant? ")

if plant == 'Spathiphyllum':
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == 'spathiphyllum':
    print("No, I want a big Spathiphyllum!")
else: 
    print("Spathiphyllum! Not", plant, end="!")