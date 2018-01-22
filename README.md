Esse exemplo foi feito utilizando Selenium Webdriver e Python3.

Para sua execução será necessario a instalação do Python3(foi utilizado 3.6 para fazer o exemplo),
do Selenium.

-Python: https://www.python.org/downloads/<br>
-Selenium Webdriver: pip install selenium
-Pymongo: pip install pymongo
<br>
<br>
Ao ser executado o script vai abrir o navegador e raspar todos os links e os textos referentes a eles no Portal da Transparencia.
Ele ira procurar por palavras chave pré-definidas no CSS do site, inserir os link no MongoDB e após isso returna a lista de todos os links.
Ao retornar a lista com todos os links, o script vai verificar link por link e raspar todos os links nos sites encontrados anteriormente.