# GeradorDeSenhas
Desenvolvi esta aplicação com o intuito de fornecer senhas complexas e dificultosas de serem descobertas.

Nele, tive como intenção criar uma interface gráfica com as três opções fornecidas no sistema.
Usei também bibliotecas para maior performace durante a aplicação, são elas:
``` tkinter ```, ``` time ```, ``` random ```

Também utilizei o ```messagebox``` do tkinter para melhor aproveitamento do software.



Neste código, a cada vez que o botão ``` start ``` é pressionado, é gerada uma nova senha.
Isso através da ```def function``` criada em sua codagem.


Toda vez que esta tecla é pressionado, ela confere se já existe um arquivo ```.txt``` com o nome de "SenhasGeradas" + o dia, mes e ano que foi rodado o código, caso não exista, será então criado.


No código, ele é compreendido desta forma:

```(f'SenhasGeradas{adaptar_item(dia)}.{adaptar_item(mes)}{ano}.txt'```

como pode ver, existe uma ```def function``` que criei para adaptar caso o número for menor que 10, ele fique com um 0 na frente, tornando assim, um padrão entre todos os números.


Logo, sempre que o ```start``` for pressionado, haverá uma checagem. Após ela ser feita, caso ja exista o arquivo, ele abrirá, copiará os dados que já contém nele, e passará juntamente à nova informação que irá entrar, sendo assism, impossível de perder as senhas geradas anteriormente.


# Cx-Freeze

Para tornar esse programa possível de ser compartilhado para outras pessoas que não tenham o python instalado, o tornei um programa executável.


para fazer isso, utilizei o ```cx_freeze```, uma ferramente com enorme utilidade para esta ocasião.

Criei um arquivo chamado ```setup.py``` para fazer com que esta ferramenta funcione. 


Após ter feito isso, abri o terminal e utilizei o comando ```python .\setup.py build```, dando assim, então, o início à criação do executável.



## Atenção
Nos arquivos desse repositório, deixei um ```.rar``` deste executável, mas não é necessário baixá-lo. Afinal, basta seguir os passos acima tendo baixado tanto o ```main.py``` quanto o ```setup.py``` e colocado-os na mesma pasta.
