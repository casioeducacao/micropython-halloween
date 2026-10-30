# CASIO Educacao | Halloween com matematica
# Atividade para o app Python da fx-CG100.
# Explore as coordenadas e compare os desenhos ao alterar os parametros.

from turtle import (penup, pendown, pencolor, pensize, goto,
                    reset, speed, hideturtle)
from math import sin, cos, pi

# A amplitude modifica a ondulacao da base.
# Experimente AMPLITUDE de 3 a 10 e ONDAS de 2 a 5.
AMPLITUDE = 6
ONDAS = 3
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

# Fundo escuro para destacar o fantasma.
poligono([(-180, -85), (180, -85), (180, 85), (-180, 85)],
         (0.12, 0.10, 0.22))

# Semicircunferencia superior: x = 58*cos(t), y = 12+58*sin(t).
contorno = []
for i in range(49):
  t = pi*i/48
  contorno.append((58*cos(t), 12+58*sin(t)))
contorno.append((-58, -48))

# A base percorre a largura com uma curva senoidal.
for i in range(65):
  u = i/64
  contorno.append((-58+116*u, -48+AMPLITUDE*sin(2*pi*ONDAS*u)))
contorno.append((58, 12))
poligono(contorno, (0.91, 0.95, 1))

# Olhos simetricos e boca eliptica.
for lado in [-1, 1]:
  elipse(lado*20, 18, 7, 11, (0.12, 0.10, 0.22))
elipse(0, -10, 9, 13, (0.12, 0.10, 0.22))
penup()
hideturtle()
