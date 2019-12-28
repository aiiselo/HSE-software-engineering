#include <iostream>
#include <ctime>
#include "header.hpp"
#include <vector>

#define SIZE 10 //размер списков
#define TIMES 1 //количество повторений цикла

using namespace std;

int main(int argc, const char * argv[]) {
    
    double time_Skip_list, time_Singly_list, time_doubly_list;
    srand((int)time(NULL));
    
    cout<<"Skip lists"<<endl; //подсчет времени для скип-листов
    SkipList sk_list;
    vector<int> array;
    double start = clock();
    for (int i=0; i<TIMES; i++){
        cout<<"INSERT PROCESS"<<endl;
        for (int j=0; j<SIZE; j++){
            int n = rand() % 100;
            array.push_back(n);
            sk_list.insertNode(n);
            sk_list.print();
        }
        cout<<"DELETE PROCESS"<<endl;
        for (int j=0; j<SIZE; j++){
            int key = rand()%array.size();
            bool flag = sk_list.find(array[key]);
            if (flag){
                sk_list.deleteNode(array[key]);
                array.erase(array.begin()+key);
            }
            sk_list.print();
        }
    }
    cout<<endl;
    double finish = clock();
    time_Skip_list = (finish - start)/CLOCKS_PER_SEC;
    start = finish = 0;
    
    cout<<"Singly linked lists"<<endl; //подсчет времени для односвязных списков
    NodeS* si_list = NULL;
    NodeS* newNodeS = NULL;
    srand((int)time(NULL));
    vector<int> arraySI;
    start = clock();
    for (int i=0; i<TIMES; i++){
        cout<<"INSERT PROCESS"<<endl;
        for (int j=0; j < SIZE; j++){
            int n = rand() % 100;
            arraySI.push_back(n);
            newNodeS = getNodeS(n);
            si_list->insertNodeS(&si_list, newNodeS);
            si_list->printList(si_list);
            cout<<endl;
        }
        cout<<"DELETE PROCESS"<<endl;
        for (int j=0; j<SIZE; j++){
            int key = rand()%arraySI.size();
            bool flag = findNodeS(si_list, arraySI[key]);
            if (flag){
                int keyV =arraySI[key];
                //cout<<keyV<<endl;
                deleteNodeS(&si_list, keyV);
                arraySI.erase(arraySI.begin()+key);
            }
            si_list->printList(si_list);
            cout<<endl;
        }
    }
    finish = clock();
    time_Singly_list = (finish - start)/CLOCKS_PER_SEC;
    
    cout<<"Doubly linked lists"<<endl; //подсчет времени для двусвязных списков
    NodeD* do_list = NULL;
    NodeD* oldNodeD = NULL;
    NodeD* newNodeD = NULL;
    srand((int)time(NULL));
    vector<int> arrayDO;
    start = clock();
    cout<<"INSERT PROCESS"<<endl;
    for (int i=0; i<TIMES; i++){
        for (int j=0; j < SIZE; j++){
            int n = rand() % 100;
            arrayDO.push_back(n);
            newNodeD = getNodeD(n);
            do_list->insertNodeD(&do_list, newNodeD);
            do_list->printListD(do_list);
            cout<<endl;
        }
        cout<<"DELETE PROCESS"<<endl;
        for (int j=0; j<SIZE; j++){
            int key = rand()%arrayDO.size();
            bool flag = findNodeD(do_list, arrayDO[key]);
            if (flag){
                int keyV =arrayDO[key];
                //cout<<keyV<<endl;
                oldNodeD = getNodeD(keyV);
                deleteNodeD(&do_list, keyV);
                arrayDO.erase(arrayDO.begin()+key);
            }
            do_list->printListD(do_list);//
            cout<<endl;
        }
    }
    finish = clock();
    time_doubly_list = (finish - start)/CLOCKS_PER_SEC;
    cout<<"Time for skip list "<<time_Skip_list<<endl<<"Time for singly linked list "<< time_Singly_list<<endl<<"Time for doubly linked list "<<time_doubly_list<<endl;
}

