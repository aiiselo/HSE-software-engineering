#include "Header.h"
#include "pch.h"
#include <stdio.h>
#include <math.h>

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

//-----Меняем местами две переменные-----
void change(int *valueFirst, int *valueSecond) {
    int change = *valueFirst;
    *valueFirst = *valueSecond;
    *valueSecond = change;
}
//-----Подсчет количества нулей в числе-----
int countZeros(int value) {
    int zeros = 0;
    if (value != 0) {
        while (value % 10 == 0) {
            zeros++;
            value = value / 10;
        }
        return zeros;
    }
}

//-----Подсчет количества разрядов в числе-----
int searchPosition(long long int value) {
    int position = 0;
    if (value == 0) { //Если второе число = 0.
        position = 1;
    }
    while (value != 0) //Если же изначально число не ноль, то делим его на 10 и считаем число разрядов.
    {
        value = value / 10;
        position = position + 1;
    }
    return position; //Возвращаем число разрядов.
}

//------Вывод числа с отступами-----
void output(long long int value, int a) {
    int k;
    if (value < 0) { //Поправка отступа для отрицательных чисел.
        k = 1;
    }
    else {
        k = 0;
    }
    for (int i = 0; i < 20 - searchPosition(value) - a - k; i++) { //Отступаем необходимое количество слева.
        printf(" ");
    }
    printf("%lli\n", value);
}

//-----Печать вводимых чисел в столбик (вместе с * и ---) -----
void makingCollumn(void) {
    output(firstNum, zeros_s);// Печать первого числа.
    for (int i = 0; i < 20 - searchPosition(firstNum) - 1 - zeros_s; i++) {// Печать *.
        printf(" ");
    }
    printf("*\n");
    output(secondNum, zeros_f);// Печать второго числа.
    for (int i = 0; i < 20 - searchPosition(firstNum) - zeros_s; i++) {// Печать ---.
        printf(" ");
    }
    for (int i = 0; i < searchPosition(firstNum) + (abs(zeros_f - zeros_s)); i++) {
        printf("-");
    }
    printf("\n");
}

//-----Расчет и вывод промежуточных чисел-----
void mathFunction(void) {
    int digit; //Число в разряде второго числа.

    for (int i = 0; i < searchPosition(secondNum); i++) {
        digit = secondNum_twin % 10;
        chislo = digit * firstNum;
        if (chislo > 0) {
            output(chislo, i + zeros_all);
            if (i == 0) {
                for (int k = 0; k < 20 - searchPosition(itog) - 1; k++) {// Печать +.
                    printf(" ");
                }
                printf("+\n");
            }
        }
        secondNum_twin = secondNum_twin / 10;
