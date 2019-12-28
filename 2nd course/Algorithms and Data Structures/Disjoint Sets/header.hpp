#ifndef header_hpp
#define header_hpp

#include <stdio.h>
#include <vector>

class DSArray{
private:
    std::vector<int> array;
    int index;
public:
    DSArray(int size){
        array.resize(size);
        index = 0;
    }
    void Create (int x);
    void Union (int x, int y);
    int Find (int x);
    ~DSArray(){
       array.clear();
    }
};

class DSTree{
private:
    std::vector<int> tree;
public:
    DSTree(int size){
        tree.resize(size);
    }
    void Create (int x);
    int Find (int x);
    void Union (int x, int y);
    ~DSTree(){
        tree.clear();
    }
};

class DSTreeRanked{
private:
    std::vector<int> treeRElements;
    std::vector<int> treeHeight;
public:
    DSTreeRanked(int size){
        treeRElements.resize(size);
        treeHeight.resize(size);
    }
    void Create (int x);
    int Find (int x);
    void Union (int x, int y);
    ~DSTreeRanked(){
        treeRElements.clear();
        treeHeight.clear();
    }
};

class DSTreeRCompr{
private:
    std::vector<int> treeRCElements;
    std::vector<int> treeRank;
public:
    DSTreeRCompr(int size){
        treeRCElements.resize(size);
        treeRank.resize(size);
    }
    void Create (int x);
    int Find (int x);
    void Union (int x, int y);
    ~DSTreeRCompr(){
        treeRCElements.clear();
        treeRank.clear();
    }
};

void fullQueue(std::vector<int> &procedure, int size);

void arrayTime(int size);
void treeTime(int size);
void treeRTime(int size);
void treeRCTime(int size);

#endif /* header_hpp */


