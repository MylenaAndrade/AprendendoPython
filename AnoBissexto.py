#Desde a introdução do calendário gregoriano (em 1582), a seguinte regra é utilizada para 
#determinar o tipo de ano:
#    *se o número do ano não for divisível por quatro, é um ano comum;
#    *caso contrário, se o número do ano não for divisível por 100, é um ano bissexto;
#    *caso contrário, se o número do ano não for divisível por 400, é um ano comum;
#    *caso contrário, é um ano bissexto.
#   O código deve fazer output de uma de duas mensagens possíveis, que são Leap year ou 
#   Common year, dependendo do valor inserido.
#Seria bom verificar se o ano introduzido cai na era Gregoriana, e faz output de um aviso
#caso contrário: Not within the Gregorian calendar period

year = int(input("Enter a year: "))

if(year<1582):
    print("Not within the Gregorian calendar period")
elif (year%4!=0):
    print("Common year")
elif (year%100!=0):
    print("Leap year")
elif (year%400!=0):
    print("Common year")
else:
    print("Leap year")

