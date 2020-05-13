SELECT DISTINCT НАЗВАНИЕ, ЛЬГОТА FROM СУДНО;

SELECT DISTINCT ПОРТ_ПРИПИСКИ FROM СУДНО;

SELECT DISTINCT ПОРТ FROM МЕСТА_ПОГРУЗКИ
UNION 
SELECT ПОРТ_СКЛАДИРОВАНИЯ FROM ГРУЗ
UNION
SELECT ПОРТ_ПРИПИСКИ FROM СУДНО;