#include <iostream>
#include <stdlib.h>
#include <vector>
#include <climits>
#include <algorithm>
#include <string>

using namespace std;

void fill_max_costs (vector<vector<int>> matrix, vector<vector<int>> &cost_matrix){
    for (int j = 1; j < matrix[0].size(); j++){
        cost_matrix[0][j] = cost_matrix[0][j-1] + matrix[0][j];
    }
    for (int i = 1; i < matrix.size(); i++){
        cost_matrix[i][0] = cost_matrix[i-1][0] + matrix[i][0];
        for (int j = 1; j < matrix[0].size(); j++){
            cost_matrix[i][j] = max(matrix[i][j]+ cost_matrix[i-1][j], matrix[i][j]+cost_matrix[i][j-1]);
        }
    }
    
}

int main(int argc, const char * argv[]) {
    int n, m, x = INT_MAX, y = INT_MAX;
    cin >> n >> m;
    vector<vector<int>> matrix(n);
    for (int i = 0; i < n; i++){ //в матрицу записываются те элементы, что лежат правее и ниже "S" или на одной линии с "S"
        for (int j = 0; j < m; j++){
            string temp;
            cin >> temp;
            if (temp == "S"){
                x = i; //запоминается смещение относительно исходной матрицы
                y = j;
                matrix[i-x].push_back(0);
            }
            else if ((i >=  x) && (j >= y)){
                matrix[i-x].push_back(stoi(temp));
            }
        }
    }
    for (int i = matrix.size() - 1; i > 0; i--){ //удаляются пустые векторы (могут появится если "S" не на 0 строке матрицы)
        if (matrix[i].empty()){
            matrix.erase(matrix.begin() + i);
        }
    }
    vector<vector<int>> s_matrix (matrix.size(), vector<int>(matrix[0].size()));
    fill_max_costs(matrix, s_matrix);
    int coins =  s_matrix[s_matrix.size() -1][s_matrix[0].size() - 1];
    int i = s_matrix.size()-1, j = s_matrix[0].size()-1; // i, j - координаты финальной нижней правой клетки
    vector<int> xi, yj; //здесь хранятся координаты пути
    xi.push_back(i);
    yj.push_back(j);
    cout << "Path:" << endl;
    while (i!=0|| j!=0){ //идем от конца к началу, выбирая клетки с наибольшим значением
        if (i == 0){
            j--;
        }
        else if (j == 0){
            i--;
        }
        else if (s_matrix[i-1][j] >= s_matrix[i][j-1]){
            i--;
        }
        else {
            j--;
        }
        xi.push_back(i);
        yj.push_back(j);
    }
    reverse(xi.begin(), xi.end());
    reverse(yj.begin(), yj.end());
    for (int i = 0; i < xi.size(); i++){
        cout << "(" << xi[i] + x << "," <<yj[i] + y <<") ";
    }
    cout << "\nCoins: " << coins;
}
