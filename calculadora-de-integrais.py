import math

w= int(input('Escolha uma funcao de 1 a 5: '))
a= float(input('Escolha o inicio do intervalo: '))
b= float(input('Escolha o fim do intervalo: '))
n=1000 #subdivisoes

#funcoes pre-definidas
def f(x):
    if w==1:
        return x**2
    elif w==2:
        return math.sin(x)
    elif w==3:
        return math.exp(x)
    elif w==4:
        return math.log(x)
    elif w==5:
        return math.sqrt(x)

#implementacao da soma de riemann usando ponto medio
def soma_riemann(f,a,b,n):
    dx=(b-a)/n
    total=0 
    for i in range(n):
        x=a+(i+0.5)*dx
        total += f(x)*dx
    return total

#resultado final 
print('Valor da integral definida eh = ', soma_riemann(f,a,b,n))
