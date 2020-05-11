# Структура программы 

## Elevator.java

Класс с сеттерами и геттерами основных атрибутов лифта: id, этаж, направление (1 - вверх, 0 - без направления, -1 - вниз), список пассажиров внутри. Также есть функция движения move() - этаж изменяется на единицу в зависимости от направления и удаляет пассажиров, которые приехали на свой этаж.

## ElevatorManager.java

Класс, управляющий движением лифта. Атрибуты: space (количество свободных мест внутри лифта), floors (количество этажей в здании), elevatorsNumber (количество лифтов в здании), список лифтов и пассажиров.

Функция run( ) запускает лифты и содержит в себе набор условий, регулирующий их движение. Также run( ) выводит логи движения лифтов.

## Main.java

Класс с главной функцией main( ), запускающий программу.

## Passenger.java

Класс с сеттерами и геттерами пассажира. Всего два атрибута: начальный этаж, на котором пассажир зашел в лифт, и этаж назначения, на котором пассажир покинет лифт.

## Request.java

Класс, создающий рандомные запросы пассажиров. Атрибуты класса: количество этажей в здании, maxPeopleOnFloor - максимальное количество людей на этаже, manager - класс-управляющий лифтом. 

# Входные и выходные данные
**Входные данные**:

Enter how many elevators are in the building >> 3
Enter how many people can be in elevator at the same moment >> 3
Enter how many floors are in the building >> 10
Enter how many people can be on the floor at the same moment >> 5

**Выходные данные**:

: = = = = = = = = = = = = = = = Log history = = = = = = = = = = = = = = = :
______________________________Iteration #1______________________________
Elevator id: 0; Current floor: 0; Direction: up; Passenger number: 0
Elevator id: 1; Current floor: 0; Direction: up; Passenger number: 0
Elevator id: 2; Current floor: 0; Direction: up; Passenger number: 0
______________________________Iteration #2______________________________
Elevator id: 0; Current floor: 1; Direction: up; Passenger number: 0
Elevator id: 1; Current floor: 1; Direction: stopped; Passenger number: 0
Elevator id: 2; Current floor: 1; Direction: stopped; Passenger number: 0
______________________________Iteration #3______________________________
Elevator id: 0; Current floor: 2; Direction: up; Passenger number: 0
Elevator id: 1; Current floor: 1; Direction: stopped; Passenger number: 0
Elevator id: 2; Current floor: 1; Direction: stopped; Passenger number: 0
______________________________Iteration #4______________________________
Elevator id: 0; Current floor: 3; Direction: down; Passenger number: 0
Elevator id: 1; Current floor: 1; Direction: stopped; Passenger number: 0
Elevator id: 2; Current floor: 1; Direction: stopped; Passenger number: 0
______________________________Iteration #5______________________________
Elevator id: 0; Current floor: 2; Direction: down; Passenger number: 3
Elevator id: 1; Current floor: 1; Direction: stopped; Passenger number: 0
Elevator id: 2; Current floor: 1; Direction: stopped; Passenger number: 0
______________________________Iteration #6______________________________
Elevator id: 0; Current floor: 1; Direction: down; Passenger number: 3
Elevator id: 1; Current floor: 1; Direction: up; Passenger number: 0
Elevator id: 2; Current floor: 1; Direction: up; Passenger number: 0
______________________________Iteration #7______________________________
Elevator id: 0; Current floor: 0; Direction: up; Passenger number: 3
Elevator id: 1; Current floor: 2; Direction: up; Passenger number: 0
Elevator id: 2; Current floor: 2; Direction: up; Passenger number: 0
______________________________Iteration #8______________________________
Elevator id: 0; Current floor: 1; Direction: up; Passenger number: 3
Elevator id: 1; Current floor: 3; Direction: up; Passenger number: 0
Elevator id: 2; Current floor: 3; Direction: up; Passenger number: 0
______________________________Iteration #9______________________________
Elevator id: 0; Current floor: 2; Direction: up; Passenger number: 3
Elevator id: 1; Current floor: 4; Direction: down; Passenger number: 3
Elevator id: 2; Current floor: 4; Direction: down; Passenger number: 0
______________________________Iteration #10______________________________
Elevator id: 0; Current floor: 3; Direction: up; Passenger number: 2
Elevator id: 1; Current floor: 3; Direction: down; Passenger number: 3
Elevator id: 2; Current floor: 3; Direction: down; Passenger number: 1
______________________________Iteration #11______________________________
Elevator id: 0; Current floor: 4; Direction: up; Passenger number: 3
Elevator id: 1; Current floor: 2; Direction: down; Passenger number: 3
Elevator id: 2; Current floor: 2; Direction: up; Passenger number: 2
______________________________Iteration #12______________________________
Elevator id: 0; Current floor: 5; Direction: up; Passenger number: 3
Elevator id: 1; Current floor: 1; Direction: down; Passenger number: 3
Elevator id: 2; Current floor: 3; Direction: up; Passenger number: 2

Process finished with exit code 130 (interrupted by signal 2: SIGINT)
