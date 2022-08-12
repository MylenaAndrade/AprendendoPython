#Um mágico júnior escolheu um número secreto. Ele escondeu-o numa variável chamada 
#secret_number. Ele quer que todos os que executam o seu programa joguem o jogo do 
#Adivinhe o número secreto, e adivinhe que número escolheu para eles. Aqueles que 
#não adivinharem o número ficarão presos num loop infinito para sempre

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number=int(input("Pick up a number: "))

while number != secret_number:
    print("\nHa ha! You're stuck in my loop")
    number=int(input("Pick up a number: "))

print("\nWell done, muggle! You are free now")