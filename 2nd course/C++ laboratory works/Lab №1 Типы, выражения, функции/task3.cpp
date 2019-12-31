//
//  task3.cpp
//  Task3
//
//  Created by Олеся Мартынюк on 09/10/2019.
//  Copyright © 2019 Olesia Martinyuk. All rights reserved.
//

#include "task3.h"
#include <iostream>
#include <vector>

using namespace std;

unsigned long long sumPrime(unsigned int hbound){
    std::vector<int> sleve;
    for (int i = 0; i < hbound ; i++){
        sleve.push_back(i);
    }
    sleve[1] = 0;
    for (int i = 2; i < hbound; i++){
        for (int j = 2*i; j < hbound; j+=i){
            sleve[j] = 0;
        }
    }
    long long int sum = 0;
    for (int i = 1; i< hbound; i++){
        sum+=sleve[i];
    }
    return sum;
}
