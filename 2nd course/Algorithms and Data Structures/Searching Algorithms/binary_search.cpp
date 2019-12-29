#include <iostream>

using namespace std;

void printArray(int arr[], int n){
    for (int i = 0 ; i < n ; i++) cout << arr[i] << " ";
    cout<<"\n";
}

void binarySearch(int arr[], int n, int arg){
    int l_w = 0, r_w = n-1, mid;
    while (l_w <= r_w){
        mid = (r_w + l_w)/2;
        cout << arr[mid] << " ";
        if (arg == arr[mid]) break;
        if (arg > arr[mid]) l_w = mid+1;
        else  r_w = mid-1;
    }
    cout<<"\n";
}
// Бинарный поиск элемента, выводящий все элементы, которые были перебраны до нужного  
int main(){
    int N, arg;
    cout << "Enter array size:\n";
    cin >> N;
    int arr[N];
    cout << "Enter array:\n";
    for (int i = 0; i < N; i++) cin >> arr[i];
    cout << "Enter number to search for:\n";
    cin >> arg;
    cout << "Initial array:\n";
    printArray(arr, N);
    cout << "Binary search:\n";
    binarySearch(arr, N, arg);
}
