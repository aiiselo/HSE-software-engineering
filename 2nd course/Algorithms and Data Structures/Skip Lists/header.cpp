#include "header.hpp"
#include <stdio.h>
#include <math.h>

using namespace std;

//============== Функции SKIP LIST ================
void SkipList::insertNode(int &value){
    Node *newNode = header;
    Node *update[MAX_LEVEL + 1];
    memset(update, 0, sizeof(Node*) * (MAX_LEVEL + 1));
    for (int i = level;i >= 0;i--)
    {
        while (newNode->forward[i] != NULL && newNode->forward[i]->value <= value) //продвигаемся вправо пока не найдем место для вставки числа
        {
            newNode = newNode->forward[i];
        }
        update[i] = newNode;
    }
    newNode = newNode->forward[0];
    if (newNode == NULL || newNode->value != value)
    {
        static bool first = true;
        if (first)
        {
            srand((unsigned)time(NULL));
            first = false;
        }
        int lvl = (int)(log((float) rand() / RAND_MAX) / log(1.-0.5));
        lvl = lvl < MAX_LEVEL ? lvl : MAX_LEVEL;
        if (lvl > level)
        {
            for (int i = level + 1;i <= lvl;i++)
            {
                update[i] = header;
            }
            level = lvl;
        }
        newNode = new Node(lvl, value);
        for (int i = 0;i <= lvl;i++)
        {
            newNode->forward[i] = update[i]->forward[i];
            update[i]->forward[i] = newNode;
        }
    }
}

void SkipList::deleteNode(int &value){
    Node *keyNode = header;
    Node *update[MAX_LEVEL + 1];
    memset (update, 0, sizeof(Node*) * (MAX_LEVEL + 1));
    for (int i = level;i >= 0;i--)
    {
        while (keyNode->forward[i] != NULL && keyNode->forward[i]->value < value)
        {
            keyNode = keyNode->forward[i];
        }
        update[i] = keyNode;
    }
    keyNode = keyNode->forward[0];
    if (keyNode->value == value)
    {
        for (int i = 0;i <= level;i++)
        {
            if (update[i]->forward[i] != keyNode)
                break;
            update[i]->forward[i] = keyNode->forward[i];
        }
        delete keyNode;
        while (level > 0 && header->forward[level] == NULL)
        {
            level--;
        }
    }
}

void SkipList::print(){
    const Node *node = header->forward[0];
    while (node != NULL)
    {
        cout << node->value;
        node = node->forward[0];
        if (node != NULL)
            cout << " - ";
    }
    cout <<endl;
}

bool SkipList::find(int &key){
    Node *searchNode = header;
    for (int i = level;i >= 0;i--)
    {
        while (searchNode->forward[i] != NULL && searchNode->forward[i]->value < key)
        {
            searchNode = searchNode->forward[i];
        }
    }
    searchNode = searchNode->forward[0];
    return searchNode != NULL && searchNode->value == key;
}

//========== Функции односвязного списка ==========

struct NodeS* getNodeS(int data){
    NodeS* newNode = (NodeS*)malloc(sizeof(struct NodeS));
    newNode->value = data;
    newNode->next = NULL;
    return newNode;
}

void NodeS::insertNodeS (NodeS** pphead, NodeS* newNode){
    NodeS* current;
    if (*pphead == NULL)
        *pphead = newNode;
    else if ((*pphead)->value >= newNode->value) {
        newNode->next = *pphead;
        *pphead = newNode;
    }
    else {
        current = *pphead;
        while (current->next != NULL && current->next->value < newNode->value)
            current = current->next;
        newNode->next = current->next;
        current->next = newNode;
    }
}

bool findNodeS (NodeS* Head, int keyValue){
    NodeS* current = Head;
    while (current != NULL){
        if (current->value == keyValue)
            return true;
        current = current->next;
    }
    return false;
}

void deleteNodeS(NodeS **head_ref, int key){
    struct NodeS* temp = *head_ref, *prev = nullptr;
    if (temp != NULL && temp->value == key)    {
        *head_ref = temp->next;
        free(temp);
        return;
    }
    while (temp != NULL && temp->value != key)    {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) return;
    prev->next = temp->next;
    free(temp);
}

void NodeS::printList (NodeS* head){
    while (head != NULL){
        cout<<head->value<<" ";
        head = head->next;
        if (head != NULL)  cout << " - ";
    }
}

//========== Функции двусвязного списка ==========

struct NodeD* getNodeD(int data){
    NodeD* newNode = (NodeD*)malloc(sizeof(struct NodeD));
    newNode->value = data;
    newNode->prev = newNode->next = NULL;
    return newNode;
}

void NodeD::insertNodeD(NodeD** head_ref, NodeD* newNode){
    NodeD* current;
    if (*head_ref == NULL)
        *head_ref = newNode;
    else if ((*head_ref)->value >= newNode->value) {
        newNode->next = *head_ref;
        newNode->next->prev = newNode;
        *head_ref = newNode;
    }
    else {
        current = *head_ref;
        while (current->next != NULL &&
               current->next->value < newNode->value)
            current = current->next;
        newNode->next = current->next;
        if (current->next != NULL)
            newNode->next->prev = newNode;
        current->next = newNode;
        newNode->prev = current;
    }
}

bool findNodeD (NodeD* Head, int keyValue){
    NodeD* current = Head;
    while (current != NULL){
        if (current->value == keyValue)
            return true;
        current = current->next;
    }
    return false;
}

void deleteNodeD (NodeD **head_ref, int key){
    struct NodeD* temp = *head_ref, *prev = nullptr;
     if (temp != NULL && temp->value == key)    {
         *head_ref = temp->next;
         free(temp);
         return;
     }
     while (temp != NULL && temp->value != key)    {
         prev = temp;
         temp = temp->next;
     }
     if (temp == NULL) return;
     if (temp->next != NULL){
         prev->next = temp->next;
         temp->next->prev = temp->prev;
     }
     else {
         prev->next = NULL;
     }
     free(temp);
}

void NodeD::printListD (NodeD* head){
    while (head != NULL){
        cout<<head->value;
        head = head->next;
        if (head != NULL)  cout << " - ";
    }
}
