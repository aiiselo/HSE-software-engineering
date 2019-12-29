#include <iostream>

using namespace std;

void printArray(int arr[], int n){
    for (int i = 0 ; i < n ; i++) cout << arr[i] << " ";
    cout<<"\n";
}

void doublingSearch(int arr[], int n, int arg){
    if (arr[0] == arg || n==1){
        cout << arr[0] << " ";
        return;
    }
    else {
        int i = 1;
        while (i < n && arr[i]<arg) i*=2;
        if (i < n && arr[i] == arg)    {
            cout<<arr[i];
            return;
        }
 
        if (arr[1] == arg)  {
            cout<<arr[1];
            return;
        }
 
        if (i == 1) {
            cout<<arr[0];
            return;
        }
        
        int l_w = i/2 + 1, r_w = min(i - 1,n-1), mid;
        while (l_w <= r_w){
            mid = (r_w + l_w)/2;
            cout << arr[mid] << " ";
            if (arg == arr[mid]) break;
            if (arg > arr[mid]) l_w = mid+1;
            else  r_w = mid-1;
        }
        cout<<"\n";
    }
}
// Экспоненцинальный поиск элемента, выводящий все элементы, которые были перебраны до нужного.
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
    cout << "Doubling search:\n";
    doublingSearch(arr, N, arg);
}
