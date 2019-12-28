#ifndef Header_h
#define Header_h

//-----Глобальные переменные-----
int firstNum; //первое перемножаемое число
int secondNum;//второе перемножаемое число
int firstNum_twin;//необходимо для парсинга второго числа
int secondNum_twin;//необходимо для второго числа
int zeros_f = 0;//кол-во нулей в первом числе по умолчанию
int zeros_s = 0;//кол-во нулей во втором числе по умолчанию
int zeros_all = 0;//zeros_f+zeros_s
long int chislo;
long long itog;

//-----Используемые функции-----
void change(int *valueFirst, int *valueSecond);
int searchPosition(long long int value);
void output(long long int value, int sign);
void makingCollumn(void);
void mathFunction(void);
int countZeros(int value);
#endif
