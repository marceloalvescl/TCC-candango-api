# TCC-candango-api

Este repositório contém a implementação de uma Rest API, utilizada pelo front-end da aplicação mobile CandanGO.
A aplicação CandanGO consiste, a grosso modo, em um app para gamificar a experiência de turismo na cidade de Brasília.
<pre>
-----------------------------------------------------------------
_REQUEST_ -Cadastrar
		-
	_url 	 = http://candango.ngrok.io/api/candango/signup
	_metodos = POST  
	_header  = Content-Type application/json
	_body    = {
					"name"     : "exemplo",
					"email"    : "exemplo@ex.lo",
					"phone"    : "(61) 98934-3409",
					"gender"   : "M",
					"state"    : "DF",
					"country"  : "Brasil",
					"password" : "senhaexemplo1"
				}
-----------------------------------------------------------------
_REQUEST_ -Logar
		-
	_url 	 = http://candango.ngrok.io/api/candango/signin
	_metodos = POST  
	_header  = Content-Type application/json
	_body    = {
					"email"    : "exemplo@ex.lo",
					"password" : "senhaexemplo1"
				}
_RESPONSE_
	_header  = Set-Cookie session=3bf0675.....412; Expires...
	_cookies = session 3bf..

-----------------------------------------------------------------
_REQUEST_ -Esqueceu a senha
		-
	_url 	 = http://candango.ngrok.io/api/candango/forgotPassword
	_metodos = POST  
	_header  = Content-Type application/json
	_body    = {
					"email"    : "exemplo@ex.lo"
				}
_RESPONSE_
	_header  = Set-Cookie session=3bf0675.....412; Expires...
	_cookies = session 3bf..




-----------------------------------------------------------------
_REQUEST_ -Dados de um Usuario    @login_required -> enviar cookie session
		-
	_url 	 = http://candango.ngrok.io/api/candango/usuario
	_metodos = GET  
	_header  = Content-Type application/json;


	_body    = {
					"email"    : "exemplo@ex.lo",
					"password" : "senhaexemplo1"
				}

</pre>
