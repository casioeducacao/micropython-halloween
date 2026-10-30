# CASIO Educacao | Halloween com matematica
# Atividade para o app Python da fx-CG100.
# Explore as coordenadas e compare os desenhos ao alterar os parametros.

from turtle import (penup, pendown, pencolor, pensize, goto,
                    reset, speed, hideturtle)
from math import sin, cos, pi

# Escala recomendada: de 0.6 a 1.0, para preservar as margens.
ESCALA = 1.0
VELOCIDADE = 0

def linha(pontos, cor, largura=1):
  penup()
  pencolor(cor)
  pensize(largura)
  goto(pontos[0][0], pontos[0][1])
  pendown()
  for x, y in pontos[1:]:
    goto(x, y)
  penup()

# Preenche um poligono com segmentos horizontais.
def poligono(pontos, cor):
  ymin = int(min([p[1] for p in pontos]))
  ymax = int(max([p[1] for p in pontos]))
  for y in range(ymin, ymax + 1):
    cortes = []
    for i in range(len(pontos)):
      x1, y1 = pontos[i]
      x2, y2 = pontos[(i + 1) % len(pontos)]
      if (y1 <= y < y2) or (y2 <= y < y1):
        cortes.append(x1 + (y-y1)*(x2-x1)/(y2-y1))
    cortes.sort()
    for i in range(0, len(cortes)-1, 2):
      linha([(cortes[i], y), (cortes[i+1], y)], cor)
  linha(pontos + [pontos[0]], cor)

# Elipse: x=cx+a*cos(t), y=cy+b*sin(t).
def elipse(cx, cy, a, b, cor):
  pontos = []
  for i in range(97):
    t = 2*pi*i/96
    pontos.append((cx+a*cos(t), cy+b*sin(t)))
  poligono(pontos, cor)

reset()
speed(VELOCIDADE)
hideturtle()

# Lua: circunferencia ao fundo para contrastar com a silhueta.
elipse(0, 8, 76, 76, (1, 0.78, 0.20))

# Uma asa e refletida no eixo vertical para construir a outra.
asa = [(8, 12), (38, 35), (72, 58), (154, 64),
       (126, 36), (144, 12), (110, 18), (96, -16),
       (68, -1), (48, -31), (28, -15), (10, -30)]
for lado in [-1, 1]:
  poligono([(lado*x*ESCALA, y*ESCALA) for x, y in asa],
           (0.12, 0.10, 0.22))

# O corpo usa elipses; as orelhas sao triangulos.
elipse(0, -5*ESCALA, 18*ESCALA, 34*ESCALA, (0.12, 0.10, 0.22))
elipse(0, 26*ESCALA, 21*ESCALA, 19*ESCALA, (0.12, 0.10, 0.22))
for lado in [-1, 1]:
  poligono([(lado*5*ESCALA, 38*ESCALA),
            (lado*18*ESCALA, 65*ESCALA),
            (lado*22*ESCALA, 32*ESCALA)], (0.12, 0.10, 0.22))
  elipse(lado*8*ESCALA, 28*ESCALA, 3*ESCALA, 4*ESCALA,
         (1, 0.78, 0.20))
penup()
hideturtle()
