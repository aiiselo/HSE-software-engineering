SELECT НАЗВАНИЕ, СТОИМОСТЬ FROM ГРУЗ WHERE МАКС_КОЛВО < 500;

SELECT DISTINCT ПОРТ FROM МЕСТА_ПОГРУЗКИ WHERE ОТЧИСЛЕНИЯ_НА_ПОГРУЗКУ > 5 OR ПРИЧАЛ LIKE '%N%';

SELECT DISTINCT НАЗВАНИЕ FROM СУДНО WHERE ПОРТ_ПРИПИСКИ = 'Одесса'