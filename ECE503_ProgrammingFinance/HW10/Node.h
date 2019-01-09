#pragma once
#ifndef NODE_H
#define NODE_H
#include <iostream>
#include <string>
using namespace std;
class Node {
	friend class LinkedList;
public:
	Node(string& name, int num) :itemName(name), itemNo(num) {
		this->next = NULL;
	}
private:
	string itemName;
	int itemNo;
	Node *next;
};

#endif // !NODE_H
