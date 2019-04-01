         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 

install python3

python --version
python3 --version

check pip3 --version (if python3 is necessary)
sudo python3 -m pip install --upgrade pip

pip3 install virtualenv

create directory:
mkdir [directory]
cd [directory]                  1

create virtual environment:
virtualenv [name]
cd [name]                       2

activate virtualenv:
source bin/activate

deactivate virtualenv:
deactivate

install django:
pip3 install django

check version
python
>>>import django
>>> django.VERSION
ctrl + d to exit

create project:
django-admin stratproject [project_name]
cd [project_name]               3

find the command and run:
python3 manage.py migrate

run python3 server
python3 manage.py runserver

-----------------------------------------------------
steps to reprodece
settings.py
>>> ALLOWED_HOSTS = ['b3d586f0439c48b1bd8859db38cfa1dc.vfs.cloud9.us-east-1.amazonaws.com']
>>> print(BASE_DIR) #under BASE_DIR
runserver.py
>>> default_port = '8080'
-----------------------------------------------------

create app:
python3 manage.py startapp blog

configuration blog/models.py

install pytz module:
pip3 install pytz

create databases:
python3 manage.py makemigrations blog
----------------------------------------
steps to reprodece
setup on_delete on foreign key
in models.py
----------------------------------------
python3 manage.py sqlmigrate blog 0001
python3 manage.py migrate

python3 manage.py createsuperuser
cofiguration:
user -- admin
mail -- admin@admin.com
pw -- it114115