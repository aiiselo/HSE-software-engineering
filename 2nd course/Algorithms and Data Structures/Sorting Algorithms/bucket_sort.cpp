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

void selectionSort(vector<float> &vector){
    if(!vector.size())
        return;
    for (int i = 0; i < vector.size(); i++){
        float minimum = distance(vector.begin(),min_element(vector.begin()+i, vector.end()));
        swap(vector[minimum], vector[i]);
    }
}

void bucketSort(vector<float> &vector){
    std::vector<std::vector<float> > buckets (vector.size()); //создаем vector.size() корзин
    float maxValue = *max_element(vector.begin(), vector.end());
    for (int i=0; i<vector.size();i++){
        int j = vector.size() * vector[i] / maxValue - 1;
        buckets[j>0?j:0].push_back(vector[i]);
    }
    for (int i=0; i<vector.size(); i++){
        selectionSort(buckets[i]);
    }
    int index = 0;
    for (int i = 0; i < vector.size(); i++)
        for (int j = 0; j < buckets[i].size(); j++)
            vector[index++] = buckets[i][j];
}

int main(int argc, const char * argv[]) {
    std::vector<float> array;
    srand(time(NULL));
    for (int i=0; i<SIZE; i++){
        array.push_back((rand()%100)/(float)(rand()%10+1));
    }
    printVector(array);
    bucketSort(array);
    cout << "After bucket sort:" << endl;
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
