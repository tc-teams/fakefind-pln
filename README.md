# Natural language processing

##  To start developing 
Para utilizar do ambiente:
```
pip3 install virtualenv
virtualenv venv
```
## Tools for the environment
Para configurar as ferramentas:
```
pip3 install -U flask
```
## Run Template

### Template one
Para executar um modulo de template
```
Utilizar somente quando não tiver uma função associada
export FLASK_APP={{PATH:module}}
export FLASK_ENV=development
flask run

http://localhost:5000/
```
### Template two
Para executar um modulo de template
```
python3 sample.py runserver

http://localhost:5000/
```

## Docker Usage

```docker

docker build -t gcloud/fakefinder-pln:1.0.0 .
docker run -d -p 80:80 --name pln -t gcloud/fakefinder-pln:1.0.0 
docker logs pln --follow

```

## Exemplos
```
from nltk.tokenize import sent_tokenize
text = "God is Great! I won a lottery."
print(sent_tokenize(text))

Output: ['God is Great!', 'I won a lottery ']

```

## Container local
```
Change $PWD ----> /code/nlp/bow
```

## Curl 
```
request:
curl -X POST -d '{"description":"ola mundo, tudo bom","news":["ola mundo","ola"]}' http://localhost:5000/ -H "Content-Type:application/json" 

response:
{"description": "ola mundo, tudo bom", "pln-process": {"ola mundo": "0.6666666666666666", "ola": "0.4"}}

```

## References 
[virtualenv](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv/)
[sumarização](https://github.com/akashp1712/nlp-akash/blob/4976f2cc65b82d25bd10ca9298ae91f9d568b0be/text-summarization/Word_Frequency_Summarization.py#L30)

## Contributing

## License
