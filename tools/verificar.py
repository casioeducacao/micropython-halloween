"""CASIO Educação: verificação local da lógica dos exemplos Halloween."""

import math
from pathlib import Path
import sys
import types

ROOT = Path(__file__).resolve().parents[1]


class RegistroTurtle(types.ModuleType):
    """Registra segmentos sem depender de uma janela gráfica."""

    def __init__(self):
        super().__init__('turtle')
        self.reset()

    def reset(self):
        self.posicao = (0, 0)
        self.abaixada = False
        self.cor = 'black'
        self.largura = 1
        self.segmentos = []
        self.pontos = []

    def penup(self):
        self.abaixada = False

    def pendown(self):
        self.abaixada = True

    def pencolor(self, cor):
        if isinstance(cor, str):
            if cor not in ('black', 'grey', 'white'):
                raise ValueError('Nome de cor fora do conjunto previsto: ' + cor)
        elif not (len(cor) == 3 and all(math.isfinite(v) and 0 <= v <= 1 for v in cor)):
            raise ValueError('Cor RGB fora do intervalo de 0 a 1')
        self.cor = cor

    def pensize(self, largura):
        if not math.isfinite(largura) or largura <= 0:
            raise ValueError('Espessura inválida')
        self.largura = largura

    def goto(self, x, y):
        if not all(math.isfinite(v) for v in (x, y)):
            raise ValueError('Coordenada não finita')
        if not (-191 <= x <= 191 and -95 <= y <= 95):
            raise ValueError('Coordenada fora da janela de projeto: ' + str((x, y)))
        self.pontos.append((x, y))
        if self.abaixada:
            self.segmentos.append((self.posicao, (x, y), self.cor, self.largura))
        self.posicao = (x, y)

    def speed(self, valor):
        if not 0 <= valor <= 10:
            raise ValueError('Velocidade fora do intervalo previsto')

    def hideturtle(self):
        pass


def executar(arquivo, parametros=None):
    """Executa uma cópia em memória, preservando o código publicado."""
    codigo = arquivo.read_text(encoding='ascii')
    for nome, valor in (parametros or {}).items():
        linhas = codigo.splitlines()
        alvos = [i for i, linha in enumerate(linhas) if linha.startswith(nome + ' = ')]
        if len(alvos) != 1:
            raise ValueError('Parâmetro ausente ou ambíguo: ' + nome)
        linhas[alvos[0]] = nome + ' = ' + repr(valor)
        codigo = '\n'.join(linhas) + '\n'
    registro = RegistroTurtle()
    anterior = sys.modules.get('turtle')
    sys.modules['turtle'] = registro
    try:
        exec(compile(codigo, str(arquivo), 'exec'), {'__name__': '__main__'})
    finally:
        if anterior is None:
            sys.modules.pop('turtle', None)
        else:
            sys.modules['turtle'] = anterior
    if not registro.segmentos:
        raise AssertionError('O programa não produziu segmentos')
    if registro.abaixada:
        raise AssertionError('A caneta deve terminar levantada')
    return registro


def verificar():
    casos = {
        'abobora.py': [None] + [dict(A=a, B=b) for a in (80, 115) for b in (50, 65)],
        'morcego.py': [None, dict(ESCALA=0.6), dict(ESCALA=1.0)],
        'fantasma.py': [None, dict(AMPLITUDE=0)] + [
            dict(AMPLITUDE=a, ONDAS=o) for a in (3, 10) for o in (2, 5)
        ],
    }
    total = 0
    for nome, variacoes in casos.items():
        arquivo = ROOT / 'exemplos' / 'halloween' / nome
        if len(arquivo.stem) > 8:
            raise AssertionError('O projeto adota nomes com até oito caracteres')
        for parametros in variacoes:
            executar(arquivo, parametros)
            total += 1
        print('OK:', nome, '-', len(variacoes), 'casos')
    print('Concluído:', total, 'casos locais. Validação no equipamento permanece separada.')


if __name__ == '__main__':
    verificar()
