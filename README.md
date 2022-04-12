# Yatube_project
### Описание
Социальная сеть для публикации личных дневников.
### Установка
- Установите и активируйте виртуальное окружение
```
python -m venv env
```
```
source env/bin/activate
```
- Установите зависимости из файла requirements.txt
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Для запуска dev сервера:
- В папке с файлом manage.py выполните команду:
```
python manage.py runserver
``` 
### Описание
Документацию к API проекта можно посмотреть по адресу:
http://127.0.0.1:8000/redoc/