#include "task4.h"

#include <iostream>
#include <string>
#include <cstring>
#include <stdio.h>
#include <algorithm>

using namespace std;

char * sum(char *x, char *y) {
    string X = x, Y = y;
    if (X.length() < Y.length()) swap(X, Y);
    reverse(X.begin(), X.end());
    reverse(Y.begin(), Y.end());
    string Z;
    int ostatok = 0, summa = 0;
    for (int i = 0; i < (int)Y.length(); i++){
        summa = (int)(X[i]-'0') + int(Y[i]-'0') + ostatok;
        ostatok = summa/10;
        summa = summa%10;
        Z.push_back(char(summa + '0'));
    }
    for (int i = (int)Y.length(); i < (int)X.length(); i++){
        summa = (int)(X[i]-'0') + ostatok;
        ostatok = summa/10;
        summa = summa%10;
        Z.push_back(char(summa + '0'));
    }
    if (ostatok) Z.push_back(char(ostatok)+'0');
    reverse(Z.begin(), Z.end());
    char res[Z.length()+1];
    for (int i=0; i< sizeof(res); i++){
        res[i] = Z[i];
    }
    return strdup(res);
}
