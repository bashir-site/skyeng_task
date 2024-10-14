# skyeng_task

Ссылка на проект: https://fannyfanny879.pythonanywhere.com/

Логин: 
```bash
admin
```
Пароль: 
```bash
admin
```

## Установка и запуск

Для начала нужно скопировать проект к себе на ПК с помощью команды:
```bash
git clone git@github.com:bashir-site/skyeng_task.git
```

Затем нужно запустить докер контейнеры с проектом и базой данных этой командой:
```bash
docker-compose up --build
```
(можно запускать с флажком -d, чтобы контейнер запустился в фоне)

После этого веб сервис будет доступе по url:
```
http://0.0.0.0:8000/
```

## Дополнительные команды

Для того, чтобы добавить 5 новых товаров, нужно запустить команду:
```bash
docker exec -it skyeng-web-1 python conf/manage.py create_products
```

## Контакты

https://t.me/bashir_77
