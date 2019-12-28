#include "header.hpp"
#include <iostream>
#include <stdio.h>
#include <vector>


using namespace std;

void DSArray::Create (int x){
    index++;
    array[x] = index;
}

void DSArray::Union (int x, int y){
    for (int i=0; i<array.size(); i++){
        if (array[i] == array[x]){
            array[x] = array[y];
        }
    }
}

int DSArray::Find (int x){
    return array[x];
}

void DSTree::Create (int x){
    tree[x]=x;
}

int DSTree::Find (int x){
    while (tree[x]!=x){
        x = tree[x];
    }
    return tree[x];
}

void DSTree::Union (int x, int y){
    x = Find(x);
    y = Find(y);
    if (x==y) return;
    tree[x]=y;
}

void DSTreeRanked::Create(int x){
    treeRElements[x]=x;
    treeHeight[x]=0;
}

void DSTreeRanked::Union(int x, int y){
    x = Find(x);
    y = Find(y);
    if (x == y) return;
    if (treeHeight[x]<treeHeight[y]) treeRElements[x]=y;
    else {
        if (treeHeight[x]>treeHeight[y]) treeRElements[y]=x;
        else {
            treeRElements[x] = y;
            treeHeight[y]++;
        }
    }
}

int DSTreeRanked::Find(int x){
    while (treeRElements[x]!=x){
        x = treeRElements[x];
    }
    return treeRElements[x];
}

void DSTreeRCompr::Create(int x){
    treeRCElements[x] = x;
    treeRank[x] = 0;
}

void DSTreeRCompr::Union(int x, int y){
    x = Find(x);
    y = Find(y);
    if (x == y) return;
    if (treeRank[x]<treeRank[y]) treeRCElements[x]=y;
    else {
        if (treeRank[x]>treeRank[y]) treeRCElements[y]=x;
        else {
            treeRCElements[x] = y;
            treeRank[y]++;
        }
    }
}

int DSTreeRCompr::Find(int x){
    int z = x;
    while (treeRCElements[x]!=x){
        x = treeRCElements[x];
    }
    int y = x;
    while (treeRCElements[z]!=z){
        int key = z;
        z = treeRCElements[z];
        treeRCElements[key] = y;
    }
    return x;
}

void fullQueue(std::vector<int> &procedure, int size) {
    procedure.clear();
    int F = size - 1; // 0
    int U = size - 1; // 1
    while ((F>0) || (U>0)){
        if ((rand() % 2 == 0) && (F>0)){
            procedure.push_back(0);
            F--;
        } else if (U>0) {
            procedure.push_back(1);
            U--;
        }
    }
}

void arrayTime(int size){
    double totalTime = 0;
    for (int k = 0; k<50; k++){
        
        srand((int)time(0));
        double startTime = 0;
        
        DSArray *array = new DSArray(size);
        startTime = clock();
        for (int i=0; i<size; i++){
            array->Create(i);
        }
        
        std::vector<int> procedure;
        fullQueue(procedure, size);
        
        for (int i = 0; i < 2*size - 2; i++){
            if (procedure[i]==0) array->Find(rand()%size);
            if (procedure[i]==1) array->Union(rand()%size, rand()%size);
        }
        
        delete array;
        double endTime = clock() - startTime;
        totalTime +=endTime;
        //cout<<"Time of iteration №"<<k+1<<" is "<<endTime/CLOCKS_PER_SEC<<endl;
        //cout<<endTime/CLOCKS_PER_SEC<<endl; //раскомментируйте, чтобы увидеть время каждой итерации
        
    }
    cout<<"\n"<<endl;
    cout<<"Total time for array of "<<size<<" elements is "<<totalTime/CLOCKS_PER_SEC<<endl;
    cout<<"Average time for array of "<<size<<" elements is "<<totalTime/(CLOCKS_PER_SEC*50)<<endl;
    cout<<"\n"<<endl;
}

void treeTime(int size){
    double totalTime = 0;
    for (int k = 0; k<50; k++){
        
        srand((int)time(0));
        double startTime = 0;
        
        DSTree *tree = new DSTree(size);
        startTime = clock();
        for (int i=0; i<size; i++){
            tree->Create(i);
        }
        
        std::vector<int> procedure;
        fullQueue(procedure, size);
        
        for (int i = 0; i < 2*size - 2; i++){
            if (procedure[i]==0) tree->Find(rand()%size);
            if (procedure[i]==1) tree->Union(rand()%size, rand()%size);
        }
        
        delete tree;
        double endTime = clock() - startTime;
        totalTime +=endTime;
        //cout<<"Time of iteration №"<<k+1<<" is "<<endTime/CLOCKS_PER_SEC<<endl;
        //cout<<endTime/CLOCKS_PER_SEC<<endl; //раскомментируйте, чтобы увидеть время каждой итерации
        
    }
    cout<<"\n"<<endl;
    cout<<"Total time for usual tree of "<<size<<" elements is "<<totalTime/CLOCKS_PER_SEC<<endl;
    cout<<"Average time for usual tree of "<<size<<" elements is "<<totalTime/(CLOCKS_PER_SEC*50)<<endl;
    cout<<"\n"<<endl;
}

void treeRTime(int size){
    double totalTime = 0;
    for (int k = 0; k<50; k++){
        
        srand((int)time(0));
        double startTime = 0;
        
        DSTreeRanked *rankedTree = new DSTreeRanked(size);
        startTime = clock();
        for (int i=0; i<size; i++){
            rankedTree->Create(i);
        }
        
        std::vector<int> procedure;
        fullQueue(procedure, size);
        
        for (int i = 0; i < 2*size - 2; i++){
            if (procedure[i]==0) rankedTree->Find(rand()%size);
            if (procedure[i]==1) rankedTree->Union(rand()%size, rand()%size);
        }
        
        delete rankedTree;
        double endTime = clock() - startTime;
        totalTime +=endTime;
        //cout<<"Time of iteration №"<<k+1<<" is "<<endTime/CLOCKS_PER_SEC<<endl;
        //cout<<endTime/CLOCKS_PER_SEC<<endl; //раскомментируйте, чтобы увидеть время каждой итерации
        
    }
    cout<<"\n"<<endl;
    cout<<"Total time for ranked tree of "<<size<<" elements is "<<totalTime/CLOCKS_PER_SEC<<endl;
    cout<<"Average time for ranked tree of "<<size<<" elements is "<<totalTime/(CLOCKS_PER_SEC*50)<<endl;
    cout<<"\n"<<endl;
}

void treeRCTime(int size){
    double totalTime = 0;
    for (int k = 0; k<50; k++){
        
        srand((int)time(0));
        double startTime = 0;
        
        DSTreeRCompr *rcTree = new DSTreeRCompr(size);
        startTime = clock();
        for (int i=0; i<size; i++){
            rcTree->Create(i);
        }
        
        std::vector<int> procedure;
        fullQueue(procedure, size);
        
        for (int i = 0; i < 2*size - 2; i++){
            if (procedure[i]==0) rcTree->Find(rand()%size);
            if (procedure[i]==1) rcTree->Union(rand()%size, rand()%size);
        }
        
        delete rcTree;
        double endTime = clock() - startTime;
        totalTime +=endTime;
        //cout<<"Time of iteration №"<<k+1<<" is "<<endTime/CLOCKS_PER_SEC<<endl;
        //cout<<endTime/CLOCKS_PER_SEC<<endl;//раскомментируйте, чтобы увидеть время каждой итерации
        
    }
    cout<<"\n"<<endl;
    cout<<"Total time for ranked tree of "<<size<<" elements is "<<totalTime/CLOCKS_PER_SEC<<endl;
    cout<<"Average time for ranked tree of "<<size<<" elements is "<<totalTime/(CLOCKS_PER_SEC*50)<<endl;
    cout<<"\n"<<endl;
}
