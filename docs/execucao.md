# Como executar os programas

## Na CASIO fx-CG100

1. Baixe um dos arquivos `.py` da pasta `exemplos/halloween/`;
2. Conecte a calculadora ao computador com um cabo USB de dados e selecione o modo de armazenamento USB, quando solicitado;
3. Copie o arquivo para a área de armazenamento acessível pelo app Python. Mantenha o nome e a extensão `.py`;
4. Ejete a unidade no computador antes de encerrar a conexão;
5. Abra o app Python na calculadora e localize o arquivo transferido;
6. Abra o programa e selecione o comando de execução disponível no app;
7. Aguarde a conclusão do desenho. O preenchimento utiliza muitos segmentos e pode levar algum tempo.

Os nomes e a localização dos comandos devem ser conferidos no manual da versão instalada. Este roteiro descreve o fluxo de transferência e execução; a sequência de telas ainda precisa ser validada na fx-CG100.

Cada programa contém suas próprias funções de desenho. Basta transferir o exemplo escolhido, sem copiar os demais arquivos do repositório.

## Personalização

Altere somente as constantes indicadas no início do programa para começar. Salve o arquivo e execute novamente após cada alteração.

| Arquivo | Parâmetro | Sugestão inicial | Efeito |
| --- | --- | --- | --- |
| `abobora.py` | `A` | De 80 a 115 | Semieixo horizontal da abóbora |
| `abobora.py` | `B` | De 50 a 65 | Semieixo vertical da abóbora |
| `morcego.py` | `ESCALA` | De 0.6 a 1.0 | Tamanho do morcego, mantendo a lua fixa |
| `fantasma.py` | `AMPLITUDE` | De 3 a 10 | Altura da ondulação na base |
| `fantasma.py` | `ONDAS` | Inteiros de 2 a 5 | Quantidade de ciclos na base |
| Todos | `VELOCIDADE` | `0` ou `6` | Velocidade solicitada ao módulo `turtle` |

Use ponto como separador decimal no código. `0` solicita o desenho sem animação intermediária, conforme o comportamento do módulo. O tempo total também depende da quantidade de segmentos e da implementação do equipamento.

## Se algo não funcionar

| Situação | O que verificar |
| --- | --- |
| O arquivo não aparece | Confirme a pasta, a extensão `.py` e se foi baixado o código original |
| Há um erro de sintaxe | Confira a indentação, os sinais e o uso de ponto nos números decimais |
| O módulo ou uma função não existe | Confira os recursos do app Python no manual do modelo e a versão do sistema |
| O desenho parece demorado | Use `VELOCIDADE = 0` e aguarde o preenchimento |
| Parte da imagem fica cortada | Restaure os valores iniciais e confira os limites de coordenadas do ambiente |

## No computador

O objetivo principal é o ambiente Python da calculadora. O `turtle` do Python para computadores depende de uma interface gráfica e pode apresentar diferenças de cores, espessuras, escala e encerramento da janela.

Para verificar a lógica sem abrir uma janela, use Python 3.10 ou superior na raiz do repositório:

```bash
python tools/verificar.py
```

Esse comando usa apenas a biblioteca padrão do computador. Ele registra as chamadas de desenho e valida a geometria nos casos verificados. Ele não é um emulador da CASIO nem comprova compatibilidade com MicroPython.
