# Preparação do repositório no GitHub

## Identidade sugerida

| Campo | Sugestão |
| --- | --- |
| Nome | `micropython-casio-educacao` |
| Descrição | Atividades de matemática e programação com MicroPython para calculadoras CASIO. Coleção inicial: Halloween na fx-CG100. |
| Tópicos | `micropython`, `casio`, `fx-cg100`, `python`, `mathematics`, `education`, `halloween`, `turtle-graphics` |

O nome abrangente permite incluir novas coleções posteriormente. Se o objetivo passar a ser manter somente esta coleção, uma alternativa é `halloween-matematico-casio`.

## Antes da publicação

- Defina a licença com a organização responsável e acrescente o arquivo `LICENSE` correspondente;
- Atualize o trecho de licenciamento no README após essa definição;
- Valide os exemplos no equipamento e registre o modelo e a versão do sistema, caso deseje publicar com a compatibilidade confirmada;
- Confira a identificação e a descrição institucional do repositório;
- Escolha a visibilidade e os responsáveis pela manutenção.

A ausência de `LICENSE` neste pacote é intencional: nenhuma permissão de distribuição foi presumida em nome da CASIO.

## Enviar os arquivos

Extraia o ZIP e envie o conteúdo da pasta `micropython-casio-educacao` para a raiz do repositório. O `README.md`, as pastas `exemplos`, `docs`, `assets` e `tools`, além da pasta `.github`, devem ficar diretamente nessa raiz.

Pelo GitHub, use o envio de arquivos do repositório. A pasta `.github` começa com um ponto e pode estar oculta no gerenciador de arquivos; confirme sua inclusão para disponibilizar os modelos e a automação.

Se preferir Git, crie primeiro um repositório vazio e execute os comandos abaixo dentro da pasta extraída:

```bash
git init
git branch -M main
git add .
git commit -m "Adiciona atividades de Halloween com MicroPython"
```

Depois, configure o endereço remoto usando a URL exata fornecida pelo GitHub e envie a branch `main`. O pacote não contém URL de organização, credenciais nem uma configuração de destino presumida.

## Manutenção

A automação verifica os programas a cada push ou pull request. Ela utiliza Python de computador com um registrador gráfico e não substitui o teste na calculadora.

Após a primeira validação no equipamento, atualize o README e as notas técnicas com os resultados observados. Acrescente novas coleções em pastas próprias dentro de `exemplos/`.
