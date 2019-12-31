//
//  main.cpp
//  Task4
//
//  Created by Олеся Мартынюк on 12/10/2019.
//  Copyright © 2019 Olesia Martinyuk. All rights reserved.
//

#include "task4.h"
#include <iostream>
#include <string>
#include <cstring>
#include <stdio.h>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    char *x="99999999999999999999";
    char *y="1";
    char *z=sum(x,y);
    cout<<z<<endl;
}
