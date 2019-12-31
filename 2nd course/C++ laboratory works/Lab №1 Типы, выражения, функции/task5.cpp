//
//  Task5.cpp
//  Task5
//
//  Created by Олеся Мартынюк on 12/10/2019.
//  Copyright © 2019 Olesia Martinyuk. All rights reserved.
//

#include "task5.h"
#include <iostream>
#include <string.h>

using namespace std;

//разбиение строки buf на подстроки и запись результата в result, с присвоением по адресу N количества полученных подстрок.

void split(char ***result, int *N, char *buf, char ch){
    string sub_str = "";
    vector<string> str;
    
    for(int i = 0;i < strlen(buf);i++){
        if(buf[i] != ch) sub_str += buf[i];
        else{
            if(sub_str.size())  str.push_back(sub_str);
            sub_str = "";
        }
    }

    if(sub_str.size()) str.push_back(sub_str); //если в конце нет запятой, а в текущей строке есть символы
    
    *N = (int)str.size();
    *result = new char*[str.size()];
    for(int  i = 0; i < str.size(); i++){
        (*result)[i] = new char[str[i].size() + 1];
        for(int j = 0;j < str[i].size();j++) (*result)[i][j] = str[i][j];
        (*result)[i][str[i].size()] = '\0';
    }

}
