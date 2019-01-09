#pragma once
#ifndef LINKEDLIST_H
#define LINKEDLIST_H
#include "Node.h"
#include <iostream>
#include <string>


class LinkedList
{
public:
	LinkedList();
	int size() const;
	void addToStart(Node *);
	void addToEnd(Node *);
	void printList();
	bool removeFromStart();
	bool removeFromEnd();
	void removeNodeFromList(int);
	void removeNodeFromList(string);
	~LinkedList();
private:
	Node *myHead;
	Node *myTail;
	int mySize;
};


#endif // !LINKEDLIST_H


