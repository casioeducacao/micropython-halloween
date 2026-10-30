# Notas técnicas

## Recursos usados

Os programas utilizam `math` para cálculos trigonométricos e `turtle` para movimentar a caneta, escolher cores e traçar segmentos. As importações são explícitas para facilitar a leitura dos recursos necessários.

Não são usados arquivos auxiliares, rede, entrada de dados pessoais ou bibliotecas instaladas por `pip`.

## Preenchimento por segmentos horizontais

A função `poligono` percorre as linhas horizontais entre a menor e a maior coordenada vertical da figura. Em cada linha, calcula as interseções com as arestas, ordena os pontos de corte e desenha os segmentos entre pares consecutivos.

A condição que inclui uma extremidade vertical e exclui a outra evita contar duas vezes uma interseção em um vértice. As arestas horizontais não entram no cálculo das interseções, evitando divisão por zero. Ao final, o contorno é traçado novamente.

Essa abordagem permite preencher polígonos côncavos, como a boca da abóbora e as asas do morcego, sem depender de funções adicionais de preenchimento do módulo gráfico.

## Aproximações de curvas

As elipses usam 96 segmentos. O topo do fantasma usa 48 segmentos e sua base é amostrada em 65 pontos. As curvas são aproximações por segmentos de reta.

A teia da abóbora conecta pontos de mesmo raio por segmentos. Suas faixas lembram arcos, mas são linhas poligonais.

Aumentar o número de amostras pode suavizar os contornos e aumentar o tempo de execução. O custo também depende da altura dos polígonos preenchidos.

## Coordenadas e limites

A composição usa a origem no centro e coordenadas cartesianas. Os testes locais adotam uma janela de projeto de `x` entre -191 e 191 e `y` entre -95 e 95. Esses limites são uma convenção de verificação do projeto, sem substituir a confirmação da área útil na versão do sistema utilizada.

Os casos de teste abrangem os valores padrão e as combinações extremas dos intervalos de personalização documentados. Alterações fora desses intervalos podem deslocar partes do desenho para fora da composição.

## Verificação e compatibilidade

`tools/verificar.py` executa os arquivos em Python de computador, substituindo `turtle` por um registrador de comandos. Ele verifica sintaxe, chamadas ao conjunto de funções previsto, valores finitos, intervalos de cores e limites geométricos.

O teste não mede memória disponível, tempo real, comportamento do módulo da CASIO ou compatibilidade com a versão de MicroPython instalada. A imagem do README deriva do mesmo tipo de registro e serve como prévia da composição.

Antes de anunciar compatibilidade validada, execute os três arquivos na calculadora ou no emulador correspondente e registre o modelo, a versão do sistema, a data e eventuais diferenças.
