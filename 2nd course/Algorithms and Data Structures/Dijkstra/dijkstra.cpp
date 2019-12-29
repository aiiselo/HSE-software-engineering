#include <iostream>
#include <vector>
#include <string>
#include <climits>
#include <algorithm>
#include <cmath>

using namespace std;

template < typename T >
void print_vector(vector <T> s){
    for (auto c : s){
        cout << c << " ";
    }
    cout << endl;
}

double find_s(double x_a, double x_b, double y_a, double y_b){
    double res = sqrt((x_a - x_b)*(x_a - x_b) + (y_a - y_b)*(y_a - y_b));
    return res;
}

int find_town_num(vector <string> s, string town){
    int i;
    for (i = 0; i < s.size(); i++){
        if (town == s[i]){
            break;
        }
    }
    return i;
}


int minDistance(double min_way[], bool marked[], int N) {
    double min = INT_MAX, min_index = 0;
    for (int i = 0; i < N; i++){
        if (marked[i] == false && min_way[i] <= min){
            min = min_way[i];
            min_index = i;
        }
    }
    return min_index;
}

double dijkstra(vector<vector<double>> graph, int f_t, int s_t, int N, vector<double> min_s, int p[]){
    double min_way[N]; //кратчайший путь до i-ой вершины
    bool marked[N];
    for (int i = 0; i < N; i++){
        min_way[i] = INT_MAX;
        marked[i] = false;
    }
    min_way[f_t] = 0;
    for (int i = 0; i < N - 1; i++) { //собственно сам алгоритм дикстры, ищущий минимальный путь
        int u = minDistance(min_way, marked, N);
        marked[u] = true;
        for (int v = 0; v < N; v++)
            if (!marked[v] && graph[u][v] && min_way[u] != INT_MAX && min_way[u] + graph[u][v] < min_way[v]) {
                min_way[v] = min_way[u] + graph[u][v];
                p[v] = u;
            }
    }
    for (int i = 0; i < N; i++){ // копируем в вектор с минимальными значениями (это я потом удалю, сейчас эта строка ничего не делает)
        min_s.push_back(min_way[i]);
    }
    return min_s[s_t]; //минимальное расстояние между заданными двумя городами
}

int main(){
    int N;
    cin >> N;
    string temp_town, temp_neighb, current_w = "";
    double temp_x, temp_y;
    vector <string> town; //город
    vector <double> x; // координата х
    vector <double> y; // координата y
    vector <vector <string>> neighbours(N); //куда проложена дорога
    for (int i = 0; i < N; i++){
        cin >> temp_town >> temp_x >> temp_y;
        getline(cin, temp_neighb);
        town.push_back(temp_town);
        x.push_back(temp_x); //кидаем координату х
        y.push_back(temp_y); // координату y
        for (auto c : temp_neighb){ //расчленяем строчку с городами после координат, далее - классические страдания
            if (c == ' '){
                if (!current_w.empty()){
                    neighbours[i].push_back(current_w);
                }
                current_w = "";
            }
            else current_w.push_back(c);
        }
        if (!current_w.empty()){
            neighbours[i].push_back(current_w);
        }
        current_w = "";
    }
    vector<vector<double>>graph(N);//матрица смежности вершин (да-да)
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++){
            vector<string>::iterator it = find(neighbours[i].begin(), neighbours[i].end(), town[j]);
            if (it != neighbours[i].end()) {
                graph[i].push_back(find_s(x[i], x[j], y[i], y[j]));
            }
            else graph[i].push_back(0);
        }
    }
    string first_town, second_town; //ввод двух городов, между которыми надо искать путь
    vector<double>min_s; //тоже ничего не делает
    vector <string> path;
    cin >> first_town >> second_town;
    int f_t = find_town_num(town, first_town); //номер первого города
    int s_t = find_town_num(town, second_town); // номер второго города
    int p[N];
    double res = dijkstra(graph, f_t, s_t, N, min_s, p); // ХОБА
    if (res < INT_MAX){
        for (int v = s_t; v != f_t; v= p[v]){
            path.push_back(town[v]);
        }
        path.push_back(town[f_t]);
        reverse(path.begin(), path.end());
        cout << "Path is not greater than " << ceil(res) << endl;
        cout << "Path:" << endl;
        print_vector<string>(path);
    }
    else {
        cout << "Path:" << endl << "No way";
    }
}
