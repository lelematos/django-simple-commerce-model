## Comados de inicialização ##
cd .. && env\scripts\activate && cd django_commerce_model 
py manage.py runserver
py manage.py makemigrations
py manage.py migrate
py manage.py shell

Modelo próprio base para criação de sites com a funcionalidade de adição de produtos, listagem, e gerenciamento de textos, imagens e links das páginas do site.

Modelo usado para desenvolver o site Julica Confeitaria, que ainda não esta 100% concluido. Link: https://julica-confeitaria.herokuapp.com/
