# calculadoracli

Para executar a aplicação, primeiramente é necessário configurar um virtualenv python.

Primeiro, execute o seguinte comando para criar o virtualenv:

`python3 -m venv virtualenv`

Em seguida, ative a virtualenv: 

`source virtualenv/bin/activate`

Após a virtualenv estar ativada, instale as dependências do projeto com o comando a seguir:

`pip install -r requirements.txt`

Pronto! Agora as dependências estão instaladas e podemos executar a CLI da calculadora.

Primeiramente, certifique-se de que tudo esteja executando normalmente, executado o comando a seguir:

`python3 main.py --help`

O esperado é que os comandos possíveis da calculadora sejam exibidos.

Após isso, é possível usar o CLI para executar operações da calculadora. 

Exemplos:

`python3 main.py -o 15 10 sum` <- 15 + 10

`python3 main.py -o 15 10 subtract` <- 15 - 10
