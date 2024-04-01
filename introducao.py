# INTRODUÇÃO AO PYTHON
nome = str(input("Diz ai teu nome:")) # ARMAZENANDO DADOS EM UMA VARIAVÉL COMO STRING
print(nome) # MOSTRANDO A VARIAVÉL
idade = int(input("Diz a tua idade:")) # ARMAZENANDO DADOS EM UMA VARIAVÉL COMO INTEIRO

print(f"E ai {nome}") #CONCATENANDO 
# ESTRUTURA DE IF/ELSE
if idade >= 18:
    print("Passa ai de maior")
else:
    print("Cai fora de menor")

# ESTRUTURA DE LOOP WHILE

print("Bem-vindo ao Oxetech!")
login = str(input("Login: "))
senha = str(input("Senha: "))

while login == senha:
    print("ERRO!! Login e Senha são iguais, tente novamente!")
    login = str(input("Login: "))
    Senha = str(input("Senha: "))
print("Login feito!")

# ESTRUTURA ARRAY
notas = [9.0, 8.9,9.9,6.0,7.5]

notas.append(10) # ADD NOTAS NO FIM DO ARRAY
notas.append(7.0)

for i in range(len(notas)): #SOMAS DE UM ARRAY
   somaNotas = sum(notas)
print(somaNotas) # IMPRIMINDO SOMA

print(notas) # MOSTRANDO A VARIAVÉL

# FUNÇÃO 

def somar (a,b):
   return a + b

soma = somar (5, 10)
print(soma)