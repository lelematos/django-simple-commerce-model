## Comados de inicialização ##
cd .. && env\scripts\activate && cd django_commerce_model 
py manage.py runserver
py manage.py makemigrations
py manage.py migrate
py manage.py shell
