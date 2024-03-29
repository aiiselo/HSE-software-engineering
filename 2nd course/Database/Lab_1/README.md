# Отчёт 

Тема: "Файловая база данных"   
Выполнила: Мартынюк Олеся   
Группа: 18ПИ-2   

## Описание выбранной предметной области БД

В качестве предметной области выбрала хранение данных о книгах. Одна запись включает в себя ID книги, её название, автора, год выпуска и цену. Теоретически, данную БД может использовать какой-нибудь букинистический магазин для хранения записей о книгах на разную тематику. 

## Что можно делать

- Добавлять новые записи (кнопка "Add new record")
- Удалять записи по ID или остальным полям (кнопка "Delete")
- Экспортировать в .csv (кнопка "Export to CSV")
- Импортировать из .csv (кнопка "Import from CSV")
- Создавать backup  (кнопка "Create back-up file")
- Читать данные из backup-файла 
- Удалить всю базу данных (кнопка "Delete database")
- Открывать (Command + O) и сохранять (Command + S)  созданные файлы
- Изменять данные прямо в даблице

Все важные события (возможные ошибки, предупреждения) в программе выводятся в отдельном окне. 

## Демонстрация работы

Продемонстрирую основные команды "Вставить" и "Удалить", остальные сложно передать через скриншоты. 

![Image before add](https://github.com/aiiselo/HSE-software-engineering/blob/master/2nd%20course/Database/Lab_1/screenshots/Снимок%20экрана%202020-05-07%20в%2004.34.42.png)
![Image after add](https://github.com/aiiselo/HSE-software-engineering/blob/master/2nd%20course/Database/Lab_1/screenshots/Снимок%20экрана%202020-05-07%20в%2004.34.54.png)

![Image before delete](https://github.com/aiiselo/HSE-software-engineering/blob/master/2nd%20course/Database/Lab_1/screenshots/Снимок%20экрана%202020-05-07%20в%2004.35.09.png)
![Image after delete](https://github.com/aiiselo/HSE-software-engineering/blob/master/2nd%20course/Database/Lab_1/screenshots/Снимок%20экрана%202020-05-07%20в%2004.35.16.png)

## Временная статистика и анализ сложности

| Number of records in DB | 10 | 100 | 1000 | 10000 | 100000 |
| --- | --- | --- | --- | --- | --- | 
| Add        |  4.61102e-05 |   4.43602e-05 |    4.91681e-05 |     0.000104972 |      0.00112887  |
| Find       |  1.0998e-06  |   7.23969e-07 |    6.88721e-07 |     7.37444e-07 |      8.51271e-07 |
| Delete     |  2.6226e-06  |   2.11954e-06 |    2.8398e-06  |     2.19033e-06 |      2.75401e-06 |

В таблице указано время в секундах на одну итерацию

График немного пьян, но вроде все в порядке: 

![image plot](https://github.com/aiiselo/HSE-software-engineering/blob/master/2nd%20course/Database/Lab_1/screenshots/Снимок%20экрана%202020-05-08%20в%2007.26.03.png)
