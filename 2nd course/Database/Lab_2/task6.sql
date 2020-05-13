SELECT НОМЕР_ВЕДОМОСТИ, ДАТА, НАЗВАНИЕ, СТОИМОСТЬ FROM ПОГРУЗКА, СУДНО WHERE
ПОГРУЗКА.СУДНО = СУДНО.ИДЕНТИФИКАТОР 
ORDER BY CASE
WHEN ДАТА = 'Понедельник' THEN 1
WHEN ДАТА = 'Вторник' THEN 2
WHEN ДАТА = 'Среда' THEN 3
WHEN ДАТА = 'Четверг' THEN 4
WHEN ДАТА = 'Пятница' THEN 5
WHEN ДАТА = 'Суббота' THEN 6
WHEN ДАТА = 'Воскресенье' THEN 7
END
, НАЗВАНИЕ;

SELECT СУДНО.НАЗВАНИЕ AS НАЗВАНИЕ_СУДНА, ПОГРУЗКА.ДАТА, МЕСТА_ПОГРУЗКИ.ПРИЧАЛ, МЕСТА_ПОГРУЗКИ.ПОРТ, ГРУЗ.НАЗВАНИЕ AS НАЗВАНИЕ_ГРУЗА FROM СУДНО, ПОГРУЗКА, МЕСТА_ПОГРУЗКИ, ГРУЗ WHERE
ПОГРУЗКА.СУДНО = СУДНО.ИДЕНТИФИКАТОР AND ПОГРУЗКА.МЕСТО_ПОГРУЗКИ = МЕСТА_ПОГРУЗКИ.ИДЕНТИФИКАТОР AND ПОГРУЗКА.ГРУЗ = ГРУЗ.ИДЕНТИФИКАТОР; 

-- ИЛИ 

SELECT СУДНО.НАЗВАНИЕ AS НАЗВАНИЕ_СУДНА, ПОГРУЗКА.ДАТА, МЕСТА_ПОГРУЗКИ.ПРИЧАЛ, ГРУЗ.НАЗВАНИЕ AS НАЗВАНИЕ_ГРУЗА FROM СУДНО, ПОГРУЗКА, МЕСТА_ПОГРУЗКИ, ГРУЗ WHERE
ПОГРУЗКА.СУДНО = СУДНО.ИДЕНТИФИКАТОР AND ПОГРУЗКА.МЕСТО_ПОГРУЗКИ = МЕСТА_ПОГРУЗКИ.ИДЕНТИФИКАТОР AND ПОГРУЗКА.ГРУЗ = ГРУЗ.ИДЕНТИФИКАТОР



