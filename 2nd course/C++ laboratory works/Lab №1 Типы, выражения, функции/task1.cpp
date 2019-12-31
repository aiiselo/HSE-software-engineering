//
//  task1.cpp
//  SoftwareLab1
//
//  Created by Олеся Мартынюк on 25/09/2019.
//  Copyright © 2019 Olesia Martinyuk. All rights reserved.
//

#include "task1.h"

unsigned long findValue(unsigned int min,unsigned max){
    int startValue = max;
    for (int i=min; i< max+1; i++){
        while (startValue%i!=0){
            startValue+=max;
            i=min;
        }
    }
    return startValue;
}
