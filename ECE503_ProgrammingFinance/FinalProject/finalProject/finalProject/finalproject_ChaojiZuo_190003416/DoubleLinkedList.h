#pragma once
#ifndef DOUBLELINKEDLIST_H
#define DOUBLELINKEDLIST_H
#include "Node.h"
#include <iostream>
#include <string>
using namespace std;

class DoubleLinkedList
{
	friend class StockAccount;
public:
	DoubleLinkedList();
	~DoubleLinkedList();

	void sort();
	Node * findNodebyPosition(int pos) const;
	void insertAtEnd(Node *);
	Node * findNodebyName(string name);
	void deleteNode(string);
	void printList();
	void swap(Node *, Node *);
	bool isNode(string);
	Node *getNode(string);
	Node * getHead();
	int getSize();
private:
	Node *pHead;
	Node *pTail;
	int listLength;
};

#endif // !DOUBLELINKEDLIST_H
