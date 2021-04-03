# TCC-candango-api

Este repositório contém a implementação de uma Rest API, utilizada pelo front-end da aplicação mobile CandanGO.
A aplicação CandanGO consiste, a grosso modo, em um app para gamificar a experiência de turismo na cidade de Brasília.
<pre>
  - Para logar:
      -REQUEST: 
          -URL: 127.0.0.1:5000/api/candango/signin
          -Método: POST
          -Body (JSON): {
                          "eml_usuario":"<email cadastrado>",
                          "pwd_usuario":"<senha cadastrada>"
                       }
          -Headers: Nenhum.
      -RESPONSE:
          -status: 200 OK
              -Headers:
                    -Content-Type: application/json
                    -Content-Length: <variavel>
                    -Access-Control-Allow-Origin: *
                    -Server: Wekzeug/1.0.1 Python/3.9.2
                    -Date: <data atual>
              -Body(JSON):{
                            "msg": "Login realizado com sucesso!",
                            "usuarioInfo": {
                                "email": "<email>",
                                "estado": "<estado>",
                                "genero": "<sexo>",
                                "id": "<id>",
                                "level": "<level>",
                                "nome": "<nome>",
                                "pais": "<pais>",
                                "quantidadeExpAtual": "<qtd>",
                                "telefone": "<telefone>"
                            }
                          }
          -status: 401 UNAUTHORIZED
              -Headers:
                    -Content-Type: application/json
                    -Content-Length: <variavel>
                    -Access-Control-Allow-Origin: *
                    -Server: Wekzeug/1.0.1 Python/3.9.2
                    -Date: <data atual>
              -Body(JSON):{
                            "msg": "Usuário ou senha incorreto"
                          }
  - Para cadastrar:
</pre>
