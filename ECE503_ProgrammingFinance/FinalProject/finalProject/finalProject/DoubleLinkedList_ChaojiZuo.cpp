#include "DoubleLinkedList.h"



DoubleLinkedList::DoubleLinkedList()
{
	this->listLength = 0;
	//set head and tail
	this->pHead = new Node("head", -1);
	this->pTail = new Node("tail", -1);
	pHead->pNext = pTail;
	pTail->pPre = pHead;
}


DoubleLinkedList::~DoubleLinkedList()
{
	Node * pCur = pHead;
	while (pCur->pNext) {
		Node *pTemp = pCur;
		pCur = pCur->pNext;
		delete pTemp;
		pTemp = NULL;

	}
	pHead = NULL;
	pTail = NULL;
	listLength = 0;
}

//bubble sort
void DoubleLinkedList::sort()
{
	
}

Node * DoubleLinkedList::findNodebyPosition(int pos) const {
	if (pos > listLength) {
		cout << "Error: wrong position" << endl;
		return nullptr;
	}
	else
	{
		Node *pTemp = pHead->pNext;
		for (int count = 1; count != pos; count++) {
			pTemp = pTemp->pNext;
			if (pTemp == pTail) {
				cout << "Error: get tail" << endl;
				break;
			}
		}
		return  pTemp;
	}
}

//insert a node at the end of the list
void DoubleLinkedList::insertAtEnd(Node * node)
{
	node->pNext = pTail;
	node->pPre = pTail->pPre;
	pTail->pPre->pNext = node;
	pTail->pPre = node;
	listLength++;
}

//find a stock by its name
Node* DoubleLinkedList::findNodebyName(string name) {
	Node *pTemp = pHead;
	while (pTemp != pTail) {
		//cout << pTemp->stockName << endl;
		if (pTemp->stockName == name) {
			return pTemp;
		}
		pTemp = pTemp->pNext;
	}
	return nullptr;
}

//delete a node by its name
void DoubleLinkedList::deleteNode(string name)
{
	Node * pTemp=findNodebyName(name);
	if (pTemp == nullptr) {
		cout << "Error: Stock Not Found!" << endl;
	}
	else {
		pTemp->pPre->pNext = pTemp->pNext;
		pTemp->pNext->pPre = pTemp->pPre;
		pTemp->pNext = NULL;
		pTemp->pPre = NULL;
		delete pTemp;
		listLength--;
	}

}

//print the list
void DoubleLinkedList::printList()
{
	Node* pTemp = pHead->pNext;
	while (pTemp != pTail) {
		cout << "Stock: " << pTemp->stockName << " Num: " << pTemp->stockNum << endl;
		pTemp = pTemp->pNext;
	}
}

//swap the order of two nodes
void DoubleLinkedList::swap(Node *lp, Node *rp)
{
	if (lp->pNext == rp) {
		lp->pPre->pNext = rp;
		lp->pNext = rp->pNext;

		rp->pNext->pPre = lp;
		rp->pPre = lp->pPre;

		lp->pPre = rp;
		rp->pNext = lp;
		
	}
	else if (lp->pPre = rp) {
		rp->pPre->pNext = lp;
		rp->pNext = lp->pNext;

		lp->pNext->pPre = rp;
		lp->pNext = rp->pPre;

		rp->pPre = lp;
		lp->pNext = rp;
	}
	else {
		Node *pTemp = new Node("", 0);

		pTemp->pNext = lp->pNext;
		pTemp->pPre = lp->pPre;

		lp->pPre->pNext = rp;
		lp->pNext->pPre = rp;

		lp->pPre = rp->pPre;
		lp->pNext = rp->pNext;

		rp->pPre->pNext = lp;
		rp->pNext->pPre = lp;

		rp->pNext = pTemp->pNext;
		rp->pPre = pTemp->pPre;

		pTemp->pNext = NULL;
		pTemp->pPre = NULL;
		delete pTemp;
	}
}

//find wheather a stock exist.
bool DoubleLinkedList::isNode(string name)
{
	Node *pTemp = pHead;
	while (pTemp->pNext != pTail) {
		if (pTemp->stockName == name) {
			return true;
		}
		pTemp = pTemp->pNext;
	}
	return false;
}

Node * DoubleLinkedList::getNode(string name)
{
	return findNodebyName(name);
}

Node * DoubleLinkedList::getHead()
{
	return pHead;
}

int DoubleLinkedList::getSize()
{
	return listLength;
}
