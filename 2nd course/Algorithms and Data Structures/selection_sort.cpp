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

void selectionSort(vector<float> &vector){
    if(!vector.size())
        return;
    for (int i = 0; i < vector.size(); i++){
        float minimum = distance(vector.begin(),min_element(vector.begin()+i, vector.end()));
        swap(vector[minimum], vector[i]);
    }
}

int main(int argc, const char * argv[]) {
    std::vector<float> array;
    srand(time(NULL));
    for (int i=0; i<SIZE; i++){
        array.push_back((rand()%100)/(float)(rand()%10+1));
    }
    printVector(array);
    printf("After selection sort:\n");
    selectionSort(array);
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
