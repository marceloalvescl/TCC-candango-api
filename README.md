# TCC-candango-api

Este repositório contém a implementação de uma Rest API, utilizada pelo front-end da aplicação mobile CandanGO.
A aplicação CandanGO consiste, a grosso modo, em um app para gamificar a experiência de turismo na cidade de Brasília.

Documentação das requisições e possíveis respostas da API:

  - Para logar:<br/>
      -REQUEST:<br/> 
          -URL: 127.0.0.1:5000/api/candango/signin<br/>
          -Método: POST<br/>
          -Body (JSON): {<br/>
                          "eml_usuario":"<email cadastrado>",<br/>
                          "pwd_usuario":"<senha cadastrada>"<br/>
                       }<br/>
          -Headers: Nenhum.<br/>
      -RESPONSE:<br/>
          -status: 200 OK<br/>
              -Headers:<br/>
                    -Content-Type: application/json<br/>
                    -Content-Length: <variavel><br/>
                    -Access-Control-Allow-Origin: *<br/>
                    -Server: Wekzeug/1.0.1 Python/3.9.2<br/>
                    -Date: <data atual><br/>
              -Body(JSON):{<br/>
                            "msg": "Login realizado com sucesso!",<br/>
                            "usuarioInfo": {<br/>
                                "email": "<email>",<br/>
                                "estado": "<estado>",<br/>
                                "genero": "<sexo>",<br/>
                                "id": "<id>",<br/>
                                "level": "<level>",<br/>
                                "nome": "<nome>",<br/>
                                "pais": "<pais>",<br/>
                                "quantidadeExpAtual": "<qtd>",<br/>
                                "telefone": "<telefone>"<br/>
                            }<br/>
                          }<br/>
          -status: 401 UNAUTHORIZED<br/>
              -Headers:<br/>
                    -Content-Type: application/json<br/>
                    -Content-Length: <variavel><br/>
                    -Access-Control-Allow-Origin: *<br/>
                    -Server: Wekzeug/1.0.1 Python/3.9.2<br/>
                    -Date: <data atual><br/>
              -Body(JSON):{<br/>
                            "msg": "Usuário ou senha incorreto"<br/>
                          }<br/>
  - Para cadastrar:<br/>
      
