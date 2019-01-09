#include "Node.h"




void Node::setPrice(double price)
{
	this->stockPrice = price;
}

void Node::setNum(int num)
{
	this->stockNum = num;
}

void Node::setName(string name)
{
	this->stockName = name;
}

string Node::getName()
{
	return stockName;
}

double Node::getPrice()
{
	return stockPrice;
}

int Node::getNum()
{
	return stockNum;
}

Node::~Node()
{

}
