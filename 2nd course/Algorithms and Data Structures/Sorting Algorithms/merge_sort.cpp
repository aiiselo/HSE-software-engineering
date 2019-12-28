#include <iostream>
#include <vector>
#include <limits.h>


using namespace std;

#define SIZE 10

void printVector(vector<float> &vector){
    for (auto const &element: vector)
        std::cout << element << ' ';
    printf("\n");
}

void mergeSort(vector<float> &vector, int begin, int end){
    if (end - begin <2){
        return;
    }
    if ( end - begin == 2){
        if (vector[begin] > vector[begin+1]){
            swap(vector[begin], vector[begin+1]);
        }
        return;
    }
    mergeSort(vector, begin, begin + (end - begin)/2);
    mergeSort(vector, begin + (end - begin)/2, end);
    std::vector<float> secondVector; // второй вектор для слияния двух отсортированных частей
    int beginFirstP = begin; //начало первой отсорт части
    int endFirstP = begin + (end - begin)/2; //конец первой отсорт части
    int beginSecondP = begin + (end - begin)/2; //начало второй отсорт части
    while (secondVector.size() != end - begin){
        if (beginFirstP >= endFirstP ||(beginSecondP < end && vector[beginSecondP] <= vector[beginFirstP])){
            secondVector.push_back(vector[beginSecondP]);
            beginSecondP++;
        }
        else {
            secondVector.push_back(vector[beginFirstP]);
            beginFirstP++;
        }
    }
    for (int i = begin; i< end; i++){ //копирование отсортированного вектора в исходный
        vector[i] = secondVector[i - begin];
    }
}

int main(int argc, const char * argv[]) {
    std::vector<float> array;
    srand(time(NULL));
    for (int i=0; i<SIZE; i++){
        array.push_back((rand()%100)/(float)(rand()%10+1));
    }
    printVector(array);
    mergeSort(array, 0, SIZE);
    cout << "After merge sort:" << endl;
    printVector(array);
    bool check = false;
    for (auto i = 0; i < array.size() - 1; i++){
        if (array[i]>array[i+1]){
            check = true;
            break;
        }
    }
    check == true ? cout << "Mistake" : cout << "Correct";
}
