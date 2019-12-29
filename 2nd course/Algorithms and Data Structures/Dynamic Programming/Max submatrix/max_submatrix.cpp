#include <iostream>
#include <vector>
#include <climits>

using namespace std;

void kadane (vector<int>array, int* global_sum){
    int local_sum = 0;
    for (int i = 0; i < array.size(); i++){
        local_sum = max(local_sum + array[i], array[i]);
        if (local_sum >= *global_sum){
            *global_sum = local_sum;
        }
    }
}

void current_submatrix(vector<vector<int>> matrix, vector<int> &temp, int L, int R, int n, int* current_sum){
    if (R == L){
        for (int i = 0; i < n; i++){
            temp[i] = matrix[i][R];
        }
    }
    else {
        for (int i = 0; i < n; i++){
            temp[i] += matrix[i][R];
        }
    }
    kadane(temp, current_sum);
}

int main(int argc, const char * argv[]) {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> matrix;
    for (int i = 0; i < n; i++){
        vector<int> temp = {} ;
        for (int j = 0; j < m; j++){
            int value;
            cin >> value;
            temp.push_back(value);
        }
        matrix.push_back(temp);
    }
    vector<int> temp(matrix.size());
    int max_sum = INT_MIN;
    for (int L = 0; L < matrix[0].size(); L++){
        for(int R = L; R < matrix[0].size(); R++){
            int current_sum = INT_MIN;
            current_submatrix(matrix, temp, L, R, n, &current_sum);
            if (current_sum > max_sum){
                max_sum = current_sum;
            }
        }
    }
    cout <<"Max submatrix: " << max_sum;
}
