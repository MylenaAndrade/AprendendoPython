#O imposto mais importante, denominado Imposto sobre o Rendimento das Pessoas Singulares (IRS ou, 
#em inglês, PIT), tinha de ser pago uma vez por ano, e foi avaliado utilizando a seguinte regra:
#     *se o rendimento do cidadão não fosse superior a 85.528 thalers, o imposto era igual a 18% do 
#      rendimento menos 556 thalers e 2 cêntimos (este era o chamado desagravamento fiscal 
#      (em inglês, tax relief))
#     *se o rendimento fosse superior a este montante, o imposto seria igual a 14.839 thalers e 2 
#     cêntimos, mais 32% do excedente acima de 85.528 thalers.
#  A sua tarefa é escrever uma calculadora de impostos.
#   *Que deve aceitar um valor de floating-point: o rendimento.
#   *A seguir, deve imprimir o imposto calculado, arredondado 
#   a thalers completos. 
#Nota: este país feliz nunca devolve dinheiro aos seus cidadãos. Se o imposto calculado for inferior a zero, 
#significa apenas que não há qualquer imposto (o imposto é igual a zero). Tenha isto em consideração durante 
#os seus cálculos.

income = float(input("Enter the annual income: "))
thalers = 85528

if income < thalers:
    tax=(income*0.18)-556.2
else:
    tax=((income-thalers)*0.32)+14839.2
    
if tax <= 0:
    tax=0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")
