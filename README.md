# python_dev_Nesterov_Igor
Это тестовое задание на стажировку Фарпост.

## Инструкция по запуску
### Установите зависимости 
```pip install -r requirements.txt```
### Сгенерируйте данные для проверки работы эндпоинтов 
```python data_generation.py```
### Запустите локальный сервер
```python app.py```
### Для проверки данных нужно выбрать любой юзернейм из таблицы logs и перейти по адресам
http://127.0.0.1:5000/api/comments/?user_login=<найденный юзернейм><br>
http://127.0.0.1:5000/api/general/?user_login=<найденный юзернейм>
