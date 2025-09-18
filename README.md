# Calculadora de Integrais com Soma de Riemann

Este projeto é um trabalho da desciplina de Cálculo II da Universidade Federal do Ceará (UFC) e tem como objetivo implementar um **método numérico de integração** em Python, utilizando a **soma de Riemann pelo ponto médio**.  
O usuário pode escolher entre algumas funções pré-definidas e calcular a integral definida em um intervalo escolhido.

## Como funciona
O programa pede:
1. A função desejada (entre 1 e 5).
2. O início do intervalo de integração `a`.
3. O fim do intervalo de integração `b`.

Em seguida, ele calcula a integral aproximada usando **1000 subdivisões**.

## Funções pré-definidas
Foram escolhidas 5 funções que representam testes unitários. 
Elas são, respectivamente, funções dos tipos: 
1. Polinomial;
2. Trigonométrica;
3. Exponencial; 
4. Logarítmica; 
5. Radical.

## Requisitos
- Python 3.x
- Biblioteca padrão `math`

## Vídeo mostrando a execução
https://youtu.be/_ZbgbJotoUE?si=svgbWcsvqwiSGf2_

## O que é a Soma de Riemann?
A **soma de Riemann** é um método numérico usado para aproximar o valor de uma integral definida.  
A ideia é dividir o intervalo [a, b] em pequenos subintervalos e calcular a área dos retângulos formados, assim a soma deles será aproximadamente a área sob a curva.

Quanto mais subdivisões (n) forem usadas, mais perto a aproximação fica do valor real da integral.  
No caso deste projeto, foi utilizada a **regra do ponto médio**, que escolhe o ponto central de cada subintervalo para calcular a altura dos retângulos, garantindo uma aproximação mais precisa.

