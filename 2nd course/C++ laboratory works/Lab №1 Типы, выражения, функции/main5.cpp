//
//  main.cpp
//  Task5
//
//  Created by Олеся Мартынюк on 12/10/2019.
//  Copyright © 2019 Olesia Martinyuk. All rights reserved.
//
#include <string.h>
#include <iostream>
#include "task5.h"

using namespace std;
//Реализовать функцию разбиения строки на подстроки с использованием символа - разделителя.
int main(int argc, const char * argv[]) {
    char *buf="123,456,789";
    int N=0;
    char **result=nullptr;
    split(&result, &N, buf, ',');
}
