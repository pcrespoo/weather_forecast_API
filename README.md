# API - Previsão do tempo

Este projeto consistiu na criação de uma API para que se pudesse coletar a previsão do tempo para determinadas cidades, nos próximos 5 dias, com status a cada 3h nos dias contemplados.

A fonte de dados foi da API OpenWeather (https://openweathermap.org/).

Para a criação da API, foi utilizado Python e duas tecnologias principais: Flask e MongoDB, além de bibliotecas adicionais (ex: requests, pymongo).

## Documentation
Para que se possa executar a aplicação criada, clone este repositório e vá até o seguinte path:
```
cd weather-api/Scripts
```
Nele, execute posteriormente:
```
activate
```
Pronto. O ambiente com o Python na versão 3.9.12 está ativo e agora volte a raiz do projeto e instale as bibliotecas e frameworks necessárias, por meio de:
```
pip install -r requirements.txt
```
Uma vez instaladas, pode-se utilizar da API.

Este projeto consistiu em 2 etapas, após criação da conta na openweather e posteriormente a criação de uma database e uma collection no MongoDB Atlas:
#### 1. Gravação de registros de previsões do tempo para algumas cidades no Brasil e no mundo
#### 2. Desenvolvimento da API para coleta desses dados salvos.

A etapa 1 foi feita através do script **weather_calls.py**. Por meio dele, passamos qual a cidade gostaríamos de extrair as previsões, por meio do seguinte comando:
```
python weather_calls.py "NOME_CIDADE"
```
Uma vez executado esse comando, faz-se uma requisição à API Geolocation, do openweather, para que se possa extrair a latitude e longitude da cidade. Com essas informações, faz-se uma segunda requisição, mas desta vez para a rota que nos devolve as previsões do tempo.

Feito isso, gravamos os resultados (no formato JSON) na collection localizada no MongoDB, via PyMongo, uma lib que permite a integração do Python com o MongoDB. 

**OBS**: as credenciais para conexão no banco, bem como a API key estão localizadas no script **credentials.py**

A etapa 2 consistiu na criação de uma API com Flask, para que pudesse extrair os dados das previsões para determinadas cidades mapeadas. O script da API é o **app.py** .Nesta API, temos duas rotas:
```
Rota 1 -  /forecasts: retorna todas as previsões do tempo, de todas as cidades salvas
Rota 2 - /forecasts/id: retorna as previsões do tempo para a cidade cuja identificação é igual a id
```
**OBS**: O campo id é um valor inteiro e para essa demo, temos 10 cidades disponíveis, com seus IDs:
```
Belo Horizonte: 6321162
Curitiba: 3464975
Sao Paulo: 3448439
Recife: 3390760
New York: 3390760
London: 2643743
Denver: 5419384
Vancouver: 5419384
Hamburg: 2911298
Rome: 3169070
```
Para executar a API, siga o comando abaixo:
```
python app.py
```
Para teste de funcionalidades da API, usou-se do Postman e abaixo o link da collection com os devidos testes:
```
https://www.postman.com/pcrespoo/workspace/raizenapi/collection/12696693-136f6e64-a36b-431a-a69f-9859619881a8?action=share&creator=12696693
```
Obrigado!