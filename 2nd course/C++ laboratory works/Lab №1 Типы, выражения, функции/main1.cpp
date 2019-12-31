//
//  main.cpp
//  SoftwareLab1
//
//  Created by Олеся Мартынюк on 25/09/2019.
//  Copyright © 2019 Olesia Martinyuk. All rights reserved.
//

#include <iostream>
#include "task1.h"

using namespace std;

//Написать программу, определяющую, какое самое маленькое положительное целое
//число делится на все числа из диапазона [1...20] без остатка.

int main(int argc, const char * argv[]) {
    cout<<findValue(1,20)<<endl;
    cout<<findValue(1,10)<<endl;
}
