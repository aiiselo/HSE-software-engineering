#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int search_min_id(vector<int> arr, vector<int> used){
    int min_id = -1;
    int min = INT_MAX;
    for (int i = 0; i < arr.size(); i++){
        if (arr[i] < min && arr[i] != 0 && used[i] == 0) {
            min = arr[i];
            min_id = i;
        }
    }
    return min_id;
}

int main(int argc, const char * argv[]) {
    int n;
    cin >> n;
    vector<vector<int>> matrix(n), paths(n), costs(n);
    vector<int> used(matrix.size());
    fill(used.begin(), used.end(), 0);
    for (int i = 0; i < matrix.size(); i++){
        for (int j = 0; j < matrix.size(); j++){
            int temp;
            cin >> temp;
            matrix[i].push_back(temp);
        }
    }
    for (int i = 0; i < n; i++){
        int counts = 0; //количество пройденных городов
        int current_cost = 0, next_town_id, current_town_id = i;
        while (counts < n){
            if (counts != n-1){
                next_town_id = search_min_id(matrix[current_town_id], used); //ищем следующий непосещенный город
                if (next_town_id != -1) { //если нашелся город, продолжаем путь
                    used[current_town_id] = 1; //отмечаем, что в этом городе уже были
                    current_cost += matrix[current_town_id][next_town_id]; //прибавляем стоимость города к общей стоимости
                    paths[i].push_back(current_town_id); //пушбэчим город, из которого уходим, в путь
                    current_town_id = next_town_id; //переходим в следующий город
                    counts++; //+1 посещенный город
                }
                else{//если город не нашелся, нужно прекратить поиск из отправной точки, paths[i] присвоить значение 0, тк нет пути
                    paths[i] = {0};
                    costs[i].push_back(0);//стоимость тоже 0
                    break;//переход к следующему стартовому городу
                }
            }
            else {
                if (matrix[current_town_id][i] != 0){
                    used[current_town_id] = 1;
                    current_cost += matrix[current_town_id][i];
                    paths[i].push_back(current_town_id);
                    counts++;
                }
                else{// если не нашли пути обратно в стартовую точку
                    paths[i] = {0};
                    costs[i].push_back(0);
                    break;
                }
            }
        }
        if (counts == n){
            paths[i].push_back(i); //пушбэчим начальную точку
            costs[i].push_back(current_cost);
        }
        fill(used.begin(), used.end(), 0);
    }
    int min_cost = INT_MAX; //минимальная стоимость пути
    int min_way_index;
    for (auto i = 0; i < costs.size(); i++){
        if (costs[i][0] < min_cost && costs[i][0] != 0){
            min_cost = costs[i][0];
            min_way_index = i;
        }
    }
    if (min_cost < INT_MAX) {
        cout << "Path:" << endl;
        for (int i = 0; i < paths[min_way_index].size(); i++){
            cout << paths[min_way_index][i] << " ";
        }
        cout << "\nCost: " << min_cost;
    }
    else {
        cout << "Lost";
    }
}
