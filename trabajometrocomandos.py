$ which python3.7
$ mkvirtualenv -p /usr/bin/python3.7 metro
$ git clone --branch cecilia https://github.com/CeciliaSol/metrodeclaraciones.git
$ cd metrodeclaraciones/
$ pip install -r requirements.txt


$ python manage.py migrate 
$ python manage.py runserver

cuando llegues aca avisame asi te ayudo a corregir el error !!  

primer problema ---actualizar django 

$ pip install -U Django

...probamos nuevamente 

$ python manage.py migrate 

segundo problema ----> TypeError: __init__() missing 1 required positional argument: 'on_delete' ...solucionado
tercer problema -----> AttributeError: module 'django.contrib.auth.views' has no attribute 'login' ...solucionado
cuarto error ------> NameError: name 'auth_views' is not defined  ....solucionado 

$ python manage.py migrate  -----> migro sin errores

python 3.7 3n ubuntu 16.04

$ sudo apt update
$ sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
$ cd /tmp
$ wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz

tar -xf Python-3.7.2.tar.xz
cd Python-3.7.2
./configure --enable-optimizations

$ make -j 1
$ sudo make altinstall
$ python3.7 --version
