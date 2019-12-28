#ifndef header_hpp
#define header_hpp

#include <iostream>
#include <stdio.h>

#define MAX_LEVEL 10

struct Node {
    int value;
    Node **forward;
    Node(int level, int &value){
        forward = new Node * [level + 1];
        memset(forward, 0, sizeof(Node*) * (level + 1));
        this->value = value;
    }
    ~Node(){
        delete [] forward;
    }
};

struct SkipList {
    Node *header;
    int value;
    int level;
    SkipList(){
        header = new Node(MAX_LEVEL, value);
        level = 0;
    }
    ~SkipList(){
        delete header;
    }
    void insertNode(int &);
    void deleteNode(int &);
    bool find(int &);
    void print();
};

struct NodeS { //односвязный список
    int value;
    NodeS *next;
    void insertNodeS  (NodeS **pphead, NodeS* newNode);
    void printList (NodeS* Node);
};

void deleteNodeS(NodeS **head_ref, int key);
bool findNodeS (NodeS* Head, int keyValue);
struct NodeS* getNodeS(int data);

struct NodeD { //двусвязный список
    int value;
    NodeD *next, *prev;
    void printListD (NodeD* Node);
    void insertNodeD (NodeD** head_ref, NodeD* newNode);
};

void deleteNodeD (NodeD **head_ref, int key);
bool findNodeD (NodeD* Head, int keyValue);
struct NodeD* getNodeD(int data);

#endif /* header_hpp */
