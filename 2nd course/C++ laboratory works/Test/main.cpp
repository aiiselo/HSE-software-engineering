//
//  main.cpp
//  test
//
//  Created by Олеся Мартынюк on 18/09/2019.
//  Copyright © 2019 Olesia Martinyuk. All rights reserved.
//

#include <iostream>
#include "task.h"
using namespace std;

int main(int argc, const char * argv[]) {
    std::cout << "Hello! How old are you?\n";
    int age;
    std::cin>>age;
    int check = ageCheck(age);
    if (check == 1){
        std::cout <<"Access granted\n";
    }
    else std::cout <<"Access denied\n";
    return 0;
}
