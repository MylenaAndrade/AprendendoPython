#passo 1: criar uma lista vazia com o nome beatles;
#passo 2: utilizar o método append() para adicionar os seguintes membros da banda à lista: 
#    John Lennon, Paul McCartney, e George Harrison;
#passo 3: utilizar o loop for e o método append() para solicitar ao utilizador que adicione 
#os seguintes membros da banda à lista: Stu Sutcliffe, e Pete Best;
#passo 4: utilizar a instrução del para remover Stu Sutcliffe e Pete Best da lista;
#passo 5: utilizar o método insert() para adicionar Ringo Starr ao início da lista.

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Step 2:", beatles)

# step 3
for i in range(1,3):
    beatles.append(input("Addiction the other member: "))
print("Step 3:", beatles)

# step 4
del beatles[-1]
del beatles[-1]

print("Step 4:", beatles)
    
# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
