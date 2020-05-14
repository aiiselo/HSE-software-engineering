-- a)

SELECT НАЗВАНИЕ, СТОИМОСТЬ FROM ГРУЗ WHERE МАКС_КОЛВО < 500

-- b)

SELECT DISTINCT ПОРТ FROM МЕСТА_ПОГРУЗКИ WHERE ОТЧИСЛЕНИЯ_НА_ПОГРУЗКУ > 5 OR ПРИЧАЛ LIKE '%N%'

-- c)

SELECT DISTINCT НАЗВАНИЕ FROM СУДНО WHERE ПОРТ_ПРИПИСКИ = 'Одесса'