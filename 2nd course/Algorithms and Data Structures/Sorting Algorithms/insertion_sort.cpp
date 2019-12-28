#include <iostream>
#include <vector>
#include <ctime>

using namespace std;

#define SIZE 10

void printVector(vector<float> &vector){
    for (auto const &element: vector)
        std::cout << element << ' ';
    printf("\n");
}

void insertionSort(vector<float> &vector, int left, int right){
    for (int i = left + 1; i <= right; i++){
        float temp = vector[i];
        int j = i - 1;
        while (vector[j] > temp && j >= left){
            vector[j+1] = vector[j];
            j--;
        }
        vector[j+1] = temp;
    }
}

int main(int argc, const char * argv[]) {
    std::vector<float> array;
    srand(time(NULL));
    for (int i=0; i<SIZE; i++){
        array.push_back((rand()%100)/(float)(rand()%10+1));
    }
    printVector(array);
    cout << "After insertion sort:" << endl;
    insertionSort(array, 0, SIZE - 1);
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
