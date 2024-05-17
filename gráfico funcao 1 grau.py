import numpy as np #pip install
import matplotlib.pyplot as plt 

'''def f(a,b,x):
    y = (a*x)+b
    return y'''

'''a = input("insira a: ")
b = input("\ninsira b: ")
x = input("\ninsira x: ")'''

def f(a,b,x):
    y = a*x + b; return y

a = int(input("\nInsira o valor de A: "))
b = int(input("\nInsira o valor de B: "))

#criando o nosso domínio (eixo X)
eixoX =  np.arange(a,10,1) #do -1o até 10 em parametro de 1 em 1
eixoY = []

for x in eixoX:
    y = f(a,b,x); eixoY.append(y)

plt.plot(eixoX, eixoY, label = f"f(x) = {a}x + {b}", color = "b")
plt.title(f"Função f(x) = {a}x + {b}")
plt.xlabel("eixo X")
plt.ylabel("eixo y")
plt.grid(True)
plt.axhline(y=0, color = "k")
plt.axvline(x=0, color = "k")
plt.show()