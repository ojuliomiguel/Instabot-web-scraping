# InstaBot: um projeto de web scraping

Este foi meu primeiro projeto (pequeno e simples) de automação/scraping que fiz em 08/2019 (*funcionado em 08/2020*). 

O instaBot surgiu da necessidade de remover seguidores em massa sem intervenção humana. Apesar das limitações que o instagram impoem sobre bots, é possível realizar bastante coisa legal.


## Funcionalidades
✔️ Login <br>
✔️ Unfollow <br>
✔️ Curtir fotos de acordo com hashtags <br>

## Setup

Para executar o projeto, (o Python 3 tem que estar instalado) você precisará especificar no arquivo [instabot.py](instabot.py) na linha 11 o path para o geckodriver de acordo com seu sistema operacional. Clique [aqui](https://github.com/mozilla/geckodriver/releases) para baixar o arquivo.

> Recomendo o uso do firefox para automação - mas você poderá usar o Chrome também. Veja a documentação do selenium para tal. 

```python
self.driver = webdriver.Firefox(executable_path=r'C:\\Users\\username\\geckodriver')
```

Após realizados os passos acima, em um terminal, instale o pacote selenium:


```console
my@user:~$ pip install selenium 
```

## Utilizando o bot


```python
from instabot import InstaBot 

if __name__ == "__main__":
    instaBot = InstaBot('@seuUserName','suaSenha') # Construtor
    instaBot.login() 
    '''
    Métodos disponíveis: 
    curtirFotos('nomeHashtag')
    unfollow() # Remove 10 seguidores a cada 5min
    '''
    #instaBot.curtirFotos('tiringa')
    instaBot.unfollow()

```

Dentro do projeto basta executar em um terminal o arquivo [main.py](main.py)
```console
my@user:~$ python main.py 
```

### :email: Contato

[instagram](https://www.instagram.com/juliomiguel.dev/)