#include <iostream>
#include <stdio.h>
#include <vector>
#include <ctime>
#include "header.hpp"

using namespace std;

int main(int argc, const char * argv[]) {
    
    arrayTime(10); //143 строка в header.cpp
    arrayTime(50);
    arrayTime(100);
    arrayTime(500);
    arrayTime(1000);
    arrayTime(5000);
    arrayTime(10000);
    
    treeTime(10); //177 строка в header.cpp
    treeTime(50);
    treeTime(100);
    treeTime(500);
    treeTime(1000);
    treeTime(5000);
    treeTime(10000);
    
    treeRTime(10); //211 строка в header.cpp
    treeRTime(50);
    treeRTime(100);
    treeRTime(500);
    treeRTime(1000);
    treeRTime(5000);
    treeRTime(10000);
    
    treeRCTime(10); //245 строка в header.cpp
    treeRCTime(50);
    treeRCTime(100);
    treeRCTime(500);
    treeRCTime(1000);
    treeRCTime(5000);
    treeRCTime(10000);
    
}
