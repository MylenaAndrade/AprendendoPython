#Em 1937, um matemático alemão chamado Lothar Collatz formulou uma hipótese 
#intrigante (ainda não provada) que pode ser descrita da seguinte forma:

#  1. tomar qualquer número inteiro não-negativo e não-nulo e nomeá-lo c0;
#  2. se for par, avalie um novo c0 como c0 ÷ 2;
#  3. caso contrário, se for ímpar, avalie um novo c0 como 3 × c0 + 1;
#  4. Se c0 ≠ 1, saltar para o ponto 2.
#  5. A hipótese diz que, independentemente do valor inicial de c0, irá sempre para 1.

c0= int(input("Pick up a number: "))
steps = 0
while c0 != 1:
    if c0 <= 0:
        break
    elif c0 % 2 == 0:
        c0= c0 // 2
        print(c0)
        steps += 1
    else:
        c0= (3 * c0) + 1
        print(c0)
        steps += 1
print("steps = ", steps)