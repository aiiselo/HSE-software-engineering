-- тут я решила изменить названия таблиц и столбцов на те, что в исходном файле

ALTER TABLE shipment RENAME COLUMN register TO НОМЕР_ВЕДОМОСТИ;
ALTER TABLE shipment RENAME COLUMN weekday TO ДАТА;
ALTER TABLE shipment RENAME COLUMN vessel TO СУДНО;
ALTER TABLE shipment RENAME COLUMN place TO МЕСТО_ПОГРУЗКИ;
ALTER TABLE shipment RENAME COLUMN cargo TO ГРУЗ;
ALTER TABLE shipment RENAME COLUMN amount TO КОЛВО;
ALTER TABLE shipment RENAME COLUMN price TO СТОИМОСТЬ;

ALTER TABLE vessel RENAME COLUMN id TO ИДЕНТИФИКАТОР;
ALTER TABLE vessel RENAME COLUMN name TO НАЗВАНИЕ;
ALTER TABLE vessel RENAME COLUMN port TO ПОРТ_ПРИПИСКИ;
ALTER TABLE vessel RENAME COLUMN exemption TO ЛЬГОТА; 

ALTER TABLE vessel RENAME TO СУДНО;
ALTER TABLE shipment RENAME TO  ПОГРУЗКА;
ALTER TABLE places RENAME TO  МЕСТА_ПОГРУЗКИ;
ALTER TABLE cargo RENAME TO ГРУЗ;

ALTER TABLE ГРУЗ RENAME COLUMN id TO ИДЕНТИФИКАТОР;
ALTER TABLE ГРУЗ RENAME COLUMN name TO НАЗВАНИЕ;
ALTER TABLE ГРУЗ RENAME COLUMN port TO ПОРТ_СКЛАДИРОВАНИЯ;
ALTER TABLE ГРУЗ RENAME COLUMN price TO СТОИМОСТЬ;
ALTER TABLE ГРУЗ RENAME COLUMN amount TO МАКС_КОЛВО;

ALTER TABLE МЕСТА_ПОГРУЗКИ RENAME COLUMN id TO ИДЕНТИФИКАТОР;
ALTER TABLE МЕСТА_ПОГРУЗКИ RENAME COLUMN pier TO ПРИЧАЛ;
ALTER TABLE МЕСТА_ПОГРУЗКИ RENAME COLUMN port TO ПОРТ;
ALTER TABLE МЕСТА_ПОГРУЗКИ RENAME COLUMN allocation TO ОТЧИСЛЕНИЯ_НА_ПОГРУЗКУ;

SELECT LPAD(ИДЕНТИФИКАТОР::text, 3, '0') as ИДЕНТИФИКАТОР, НАЗВАНИЕ, ПОРТ_ПРИПИСКИ, ЛЬГОТА FROM СУДНО;
SELECT LPAD(ИДЕНТИФИКАТОР::text, 3, '0') as ИДЕНТИФИКАТОР, ПРИЧАЛ, ПОРТ, ОТЧИСЛЕНИЯ_НА_ПОГРУЗКУ FROM МЕСТА_ПОГРУЗКИ;
SELECT LPAD(ИДЕНТИФИКАТОР::text, 3, '0') as ИДЕНТИФИКАТОР, НАЗВАНИЕ, ПОРТ_СКЛАДИРОВАНИЯ, СТОИМОСТЬ, МАКС_КОЛВО FROM ГРУЗ;
SELECT НОМЕР_ВЕДОМОСТИ, ДАТА, LPAD(СУДНО::text, 3, '0') as СУДНО, LPAD(МЕСТО_ПОГРУЗКИ::text, 3, '0') as МЕСТО_ПОГРУЗКИ, LPAD(ГРУЗ::text, 3, '0') as ГРУЗ, КОЛВО, СТОИМОСТЬ FROM ПОГРУЗКА;