INSERT INTO vessel (id, name, port, exemption) VALUES (001, 'Балтимор', 'Одесса', 3);
INSERT INTO vessel (id, name, port, exemption) VALUES (002, 'Генуя', 'Одесса', 3);
INSERT INTO vessel (id, name, port, exemption) VALUES (003, 'ТПР-123', 'Владивосток', 5);
INSERT INTO vessel (id, name, port, exemption) VALUES (004, 'Ф. Шаляпин', 'Мурманск', 6);
INSERT INTO vessel (id, name, port, exemption) VALUES (005, 'Рейн', 'Калининград', 4);
INSERT INTO vessel (id, name, port, exemption) VALUES (006, 'Россия', 'Владивосток', 5);

INSERT INTO places (id, pier, port, allocation) VALUES (001, 'Северный', 'Одесса', 3);
INSERT INTO places (id, pier, port, allocation) VALUES (002, 'Южный', 'Одесса', 4);
INSERT INTO places (id, pier, port, allocation) VALUES (003, 'N1', 'Владивосток', 2);
INSERT INTO places (id, pier, port, allocation) VALUES (004, 'N2', 'Владивосток', 2);
INSERT INTO places (id, pier, port, allocation) VALUES (005, 'N3', 'Владивосток', 2);
INSERT INTO places (id, pier, port, allocation) VALUES (006, 'Основной', 'Калининград', 4);

INSERT INTO cargo (id, name, port, price, amount) VALUES (001, 'Рис', 'Одесса', 100000, 700);
INSERT INTO cargo (id, name, port, price, amount) VALUES (002, 'Зерно', 'Одесса', 80000, 890);
INSERT INTO cargo (id, name, port, price, amount) VALUES (003, 'Хлопок', 'Одесса', 300000, 400);
INSERT INTO cargo (id, name, port, price, amount) VALUES (004, 'Сахар', 'Владивосток', 140000, 600);
INSERT INTO cargo (id, name, port, price, amount) VALUES (005, 'Соль', 'Мурманск', 120000, 700);
INSERT INTO cargo (id, name, port, price, amount) VALUES (006, 'Скобяные изделия', 'Калининград', 300000, 140);
INSERT INTO cargo (id, name, port, price, amount) VALUES (007, 'Древесина', 'Мурманск', 400000, 260);
INSERT INTO cargo (id, name, port, price, amount) VALUES (008, 'Уголь', 'Владивосток', 400000, 400);

INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70204, 'Понедельник', 001, 005, 002, 100, 8000000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70205, 'Понедельник', 003, 003, 006, 4, 1200000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70206, 'Вторник', 001, 005, 007, 2, 800000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70207, 'Вторник', 002, 005, 001, 20, 2000000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70208, 'Вторник', 005, 005, 002, 3, 240000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70209, 'Среда', 003, 003, 006, 4, 1200000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70210, 'Среда', 004, 001, 001, 70, 7000000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70211, 'Среда', 004, 002, 006, 1, 300000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70212, 'Среда', 004, 002, 001, 10, 1000000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70213, 'Четверг', 001, 006, 003, 20, 6000000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70214, 'Четверг', 003, 004, 002, 2, 16000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70215, 'Четверг', 004, 003, 004, 30, 4200000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70216, 'Суббота', 003, 002, 005, 10, 1200000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70217, 'Суббота', 002, 003, 008, 20, 8000000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70218, 'Суббота', 001, 001, 001, 20, 2000000);
INSERT INTO shipment (register, weekday, vessel, place, cargo, amount, price) VALUES (70219, 'Суббота', 005, 006, 004, 10, 1400000)