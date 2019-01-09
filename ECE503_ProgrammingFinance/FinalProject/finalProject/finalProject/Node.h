#pragma once
#ifndef NODE_H
#define NODE_H
#include <string>
using namespace std;

class Node
{
	friend class DoubleLinkedList;
	friend class StockAccount;
public:
	Node(string Name, int Num) :
		stockName(Name), stockNum(Num), stockPrice(0.0),pPre(NULL),pNext(NULL)
	{}
	void setPrice(double);
	void setNum(int);
	void setName(string);
	string getName();
	double getPrice();
	int getNum();
	~Node();

private:
	Node *pPre;
	Node *pNext;

	string stockName;
	double stockPrice;
	int stockNum;
};
#endif // !NODE_H

