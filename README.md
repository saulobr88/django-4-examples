# django-4-examples

## como usar:

1 - criar virtual env (`python -m venv venv`) e ativa-lo (`source ./venv/bin/activate`)

2 - Usar o pip para instalar as dependencias (`pip install -r requirements.txt`)

3 - Executar as migrations sobre o SQLite (Padrão do Django) (`python manage.py migrate`)

4 - Criar o superusuário (django-admin) (`python manage.py createsuperuser`)

5 - Criar algumas entidades 'campos' e 'atividades'

6 - Continuar seguindo as instruções da [playlist](https://www.youtube.com/playlist?list=PLjv17QYEBJPpd6nI-MXpIa4qR7prKfPQz)

## SQLite3

Para importar os dados das tabelas `cadastros_estado` e `cadastros_cidade`, basta carregar os dados dos respectivos arquivos:

```
$ sqlite3 db.sqlite3
Enter ".help" for usage hints.
sqlite> .read cadastros_estado.sql
sqlite> .read cadastros_cidade.sql
sqlite> .quit
```

O procedimento acima é baseado nas instruções em [SQLite - How to copy data from one database to another?
](https://tableplus.com/blog/2018/07/sqlite-how-to-copy-table-to-another-database.html)
