# CASIO Educacao | Halloween com matematica
# Atividade para o app Python da fx-CG100.
# Explore as coordenadas e compare os desenhos ao alterar os parametros.

from turtle import (penup, pendown, pencolor, pensize, goto,
                    reset, speed, hideturtle)
from math import sin, cos, pi, sqrt

# Altere A (80 a 115) e B (50 a 65) para comparar proporcoes.
A = 108
B = 64
CY = -9
# 0 = mais rapido. Experimente 6 para acompanhar o tracado.
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

# Coordenadas do rosto relativas ao tamanho da abobora.
def rosto(pontos):
  poligono([(A*x, CY+B*y) for x,y in pontos], "black")

reset()
speed(VELOCIDADE)
hideturtle()

# Caule e corpo.
poligono([(-12,CY+B-3),(-10,CY+B+22),
          (7,CY+B+26),(14,CY+B+19),(5,CY+B-3)],
         (0.16,0.40,0.17))
elipse(0, CY, A, B, (1,0.47,0.04))

# Gomos: arcos elipticos. u percorre a altura normalizada.
for k in [-0.67,-0.34,0.34,0.67]:
  pontos = []
  for i in range(65):
    u = -1 + 2*i/64
    pontos.append((k*A*sqrt(max(0,1-u*u)), CY+B*u))
  linha(pontos, (0.77,0.29,0.02), 2)

# Olhos, nariz e boca simetricos.
for lado in [-1,1]:
  rosto([(lado*0.20,0.14),(lado*0.38,0.55),
         (lado*0.60,0.14)])
rosto([(-0.10,-0.08),(0,0.14),(0.10,-0.08)])
rosto([(-0.69,-0.18),(-0.45,-0.33),(-0.28,-0.27),
       (-0.15,-0.39),(0,-0.31),(0.15,-0.39),
       (0.28,-0.27),(0.45,-0.33),(0.69,-0.18),
       (0.48,-0.59),(0.30,-0.51),(0.14,-0.66),
       (0,-0.55),(-0.14,-0.66),(-0.30,-0.51),
       (-0.48,-0.59)])

# Teia: raios e arcos com o mesmo centro.
WX, WY = 179, 83
for i in range(5):
  t = pi + i*pi/8
  linha([(WX,WY),(WX+52*cos(t),WY+52*sin(t))], "grey")
for r in [13,26,39,52]:
  pontos = []
  for i in range(5):
    t = pi + i*pi/8
    pontos.append((WX+r*cos(t),WY+r*sin(t)))
  linha(pontos, "grey")

# Aranha suspensa: elipses e segmentos refletidos.
SX, SY = -153, 26
linha([(SX,83),(SX,SY+13)], "grey")
for lado in [-1,1]:
  for i in range(4):
    y = SY + 6 - 4*i
    linha([(SX+lado*6,y),(SX+lado*16,y+6),
           (SX+lado*24,y-3)], "black", 2)
elipse(SX,SY,8,11,"black")
elipse(SX,SY+11,5,5,"black")
penup()
hideturtle()
