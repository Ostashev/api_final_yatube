Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:Ostashev/api_final_yatube.git
cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python3.9 -m venv venv
source venv/bin/activate
Установить зависимости из файла requirements.txt:

python3.9 -m pip install --upgrade pip
pip install -r requirements.txt
Выполнить миграции:

python3.9 manage.py migrate
Запустить проект:

python3.9 manage.py runserver
