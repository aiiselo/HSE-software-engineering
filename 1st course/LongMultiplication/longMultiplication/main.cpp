#include "pch.h"
#include "Header.h"
#include <stdio.h>
#include <Windows.h>
#include <conio.h>
#include <locale.h>
#include <math.h>
#include <limits.h>

//-----Глобальные переменные-----
extern int firstNum;
extern int secondNum;
extern int firstNum_twin;
extern int secondNum_twin;
extern int zeros_f;
extern int zeros_s;
extern int zeros_all;
extern long int chislo;
extern long long itog;

int main() {
    system("color F0");
    setlocale(LC_ALL, "Rus");
    printf("Введите первое число: \n");
    scanf_s("%d", &firstNum);
    printf("Введите второе число: \n");
    scanf_s("%d", &secondNum);
    itog = (long long)firstNum * (long long)secondNum; //Считаем произведение заранее.     Дальше будем "рубить" числа:
    if (itog != 0) {
        zeros_f = countZeros(firstNum); //Считаем кол-во нулей в первом числе.
        zeros_s = countZeros(secondNum);//Считаем кол-во нулей во втором числе.
        zeros_all = zeros_f + zeros_s; //Общее число нулей.
        firstNum_twin = firstNum / pow(10, zeros_f);
        secondNum_twin = secondNum / pow(10, zeros_s);
        if (abs(firstNum_twin) < abs(secondNum_twin)) { //Меняем местами большее по модулю число с меньшим и их копии.
            change(&firstNum, &secondNum);
            change(&firstNum_twin, &secondNum_twin);
            change(&zeros_f, &zeros_s);
        }
        printf("Умножим эти числа в столбик: \n");//пожалуйста, поставьте 10
        makingCollumn();
        firstNum_twin = abs(firstNum_twin);
        secondNum_twin = abs(secondNum_twin);
        secondNum = secondNum_twin; //Используем модули чисел для промежуточного умножения.
        firstNum = firstNum_twin;
        if (searchPosition(secondNum) > 1) {
            mathFunction();
            for (int i = 0; i < 20 - searchPosition(itog); i++) {
                printf(" ");
            }
            for (int i = 0; i < searchPosition(itog) + 1; i++) {
                printf("-");
            }
            printf("\n");
        }
        output(itog, 0);//Вывод произведения.
    }
    else {
        if (abs(firstNum) < abs(secondNum)) { //Меняем местами большее по модулю число с меньшим и их копии.
            change(&firstNum, &secondNum);
        }
        output(firstNum, 0);
        for (int i = 0; i < 20 - searchPosition(firstNum) - 1; i++) {// Печать *.
            printf(" ");
        }
        printf("*\n");
        output(secondNum, zeros_f);
        for (int i = 0; i < 20 - searchPosition(firstNum) - zeros_s; i++) {// Печать ---.
            printf(" ");
        }
        for (int i = 0; i < searchPosition(firstNum); i++) {
            printf("-");
        }
        printf("\n");
        output(0, 0);
    }
    _getch();
}
