# Natural language processing

##  To start developing 
Para utilizar do ambiente:
```
pip3 install virtualenv
virtualenv venv
```
## tools for the environment
Para configurar as ferramentas:
```
pip3 install -U flask
```
## Run tamplete exemplo 1
Para executar um modulo de tamplete
```
Utilizar somento quando não tiver uma função associada
export FLASK_APP={{PATH:module}}
export FLASK_ENV=development
flask run

http://localhost:5000/
```
## Run tamplete exemplo 2
Para executar um modulo de tamplete
```
python3 simple.py runserver

http://localhost:5000/
```

## Exec cts_tokenize
```
from nltk.tokenize import sent_tokenize
text = "God is Great! I won a lottery."
print(sent_tokenize(text))

Output: ['God is Great!', 'I won a lottery ']

```

## Container local
```
Change $PWD ----> /code/natural-language-processing/bag-of-words
```

## Curl 
```
request:
curl -X POST -d '{"description":"ola mundo, tudo bom","news":["ola mundo","ola"]}' http://localhost:5000/ -H "Content-Type:application/json" 

response:
{"ola":"0.4","ola mundo":"0.6666666666666666"}



```




## References 
[virtualenv](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv/)

## Contributing

## License
