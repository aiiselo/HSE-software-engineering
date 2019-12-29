#include <iostream>

using namespace std;

void printArray(int arr[], int n){
    for (int i = 0 ; i < n ; i++) cout << arr[i] << " ";
    cout<<"\n";
}

void linearSearch(int arr[], int n, int arg ){
    for (int i = 0 ; i < n; i++){
        if (arr[i] == arg) {
            cout << arr[i] << " ";
            break;
        }
        if (arr[i] != arg ) cout << arr[i] << " ";
    }
    cout<<"\n";
}

// Линейный поиск элемента, выводящий все элементы, которые были перебраны до нужного.
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
    cout << "Linear search:\n";
    linearSearch(arr, N, arg);
}
