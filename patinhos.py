numPatinhos = int(input("Digite a quantidade de patos: "))

while numPatinhos < 2:
 print("ERRO: o número de patinhos deve ser >= 2")
 numPatinhos = int(input("Digite a quantidade de patos: "))

patos = numPatinhos
while patos >= 1:
 print(str(patos)+" patinhos\nForam passear" if patos>1 else "1 patinho foi passear")
 print("Além das montanhas\n"+
"Para brincar\n"+
"A mamãe gritou\n"+
"Quack quack quack")
 if patos == 2:
   print("Mas só "+str(patos-1)+" patinho\nVoltou de lá\n")
 elif patos==1:
   print("Mas nenhum patinho\nVoltou de lá\n")
 else:
   print("Mas só "+str(patos-1)+" patinhos\nVoltaram de lá\n")
 patos -= 1

print("A mamãe patinha\n"+
"Foi procurar\n"+
"Além das montanhas\n"+
"Na beira do mar\n"+
"A mamãe gritou\n"+
"Quack quack quack\n"+
"E os "+str(numPatinhos)+" patinhos\n"+
"Voltaram de lá")