# Halloween matemático em sala

## Proposta

Investigar a relação entre uma expressão matemática, suas coordenadas e uma figura construída por programação. O professor pode ajustar a profundidade conforme o conhecimento da turma sobre plano cartesiano, trigonometria e Python.

Uma sequência inicial pode ocupar de 30 a 50 minutos, dependendo do tempo de execução no equipamento e da familiaridade dos estudantes com o app Python.

## 1. Abóbora: proporção e simetria

Abra `abobora.py`. O corpo é uma elipse construída pelas relações:

```text
x = cx + a*cos(t)
y = cy + b*sin(t)
```

Na atividade, `a` e `b` são os semieixos. As constantes `A` e `B` controlam essas medidas no corpo da abóbora.

- Compare `A = 108` com `A = 85`, mantendo `B = 64`;
- Explique o que acontece com a razão entre largura e altura;
- Localize no código a multiplicação por `lado` e explique como ela gera os dois olhos;
- Investigue por que a teia utiliza seno e cosseno para distribuir seus pontos.

Desafio: altere as coordenadas da boca preservando sua simetria em relação ao eixo vertical.

## 2. Morcego: reflexão e escala

Abra `morcego.py`. O programa descreve uma asa e reflete suas coordenadas para obter a outra:

```text
(x, y) → (-x, y)
```

- Identifique quais coordenadas mudam de sinal;
- Compare `ESCALA = 1.0` com `ESCALA = 0.7`;
- Explique por que a lua permanece com o mesmo tamanho;
- Calcule a distância entre dois pontos correspondentes das asas antes e depois da mudança de escala.

Desafio: deslocar o morcego inteiro 10 unidades para cima. Aplique o mesmo deslocamento às asas, ao corpo, à cabeça, às orelhas e aos olhos.

## 3. Fantasma: amplitude e oscilações

Abra `fantasma.py`. A base do contorno usa:

```text
y = -48 + AMPLITUDE*sin(2*pi*ONDAS*u)
```

O parâmetro `u` percorre o intervalo de 0 a 1. Para valores inteiros positivos, `ONDAS` determina o número de ciclos nesse intervalo.

- Compare `AMPLITUDE = 3` com `AMPLITUDE = 10`, mantendo `ONDAS = 3`;
- Compare `ONDAS = 2` com `ONDAS = 5`, mantendo `AMPLITUDE = 6`;
- Explique por que alterar a amplitude não altera o número de oscilações;
- Preveja o aspecto da base com `AMPLITUDE = 0` e confira o resultado.

Desafio: com amplitude 6, determine os valores máximo e mínimo de `y` na curva ideal. Depois, investigue se os 65 pontos amostrados atingem exatamente esses extremos.

## Registro da investigação

Para cada alteração, registre a hipótese, o parâmetro modificado, o resultado observado e a explicação matemática. Uma captura do desenho pode complementar a resposta, desde que acompanhada da interpretação das mudanças.
