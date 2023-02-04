__Comando__

```pytest```: executa todos os testes do projeto

__Tags__:

```-v```: torna a saída dos testes no terminal mais verbosa
```-k```: executa testes que contenham palavras específicas. Por exemplo: ```pytest -k app```.

__Coverage__:

```pytest --cov```: exibe um relatório de cobertura de testes
```pytest --cov=path-code path-test```: executa a análise de cobertura apenas na pasta que contém códigos que não são de testes.
```pytest --cov=path-code tests --cov-report term-missing```: exibe o relatório de cobertura de testes, e aponta as linhas de código que não possuem cobertura.
```pytest --cov=codigo tests/ --cov-report html```: cria um relatório de cobertura de testes em um arquivo HTML interativo.
