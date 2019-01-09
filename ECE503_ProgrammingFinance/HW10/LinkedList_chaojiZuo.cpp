#include "LinkedList.h"
using namespace std;

//constructor
LinkedList::LinkedList()
{
	myHead = NULL;
	myTail = NULL;
	mySize = 0;
}
//get size of list
int LinkedList::size() const {
	return mySize;
}

//add the new node at the begin of list
void LinkedList::addToStart(Node * newNode) {
	if (mySize == 0) {
		myHead = newNode;
		myTail = newNode;
	}
	else {
		newNode->next = myHead;
		myHead = newNode;
	}
	mySize++;
}

//add the new node at the end of the list
void LinkedList::addToEnd(Node* newNode) {
	if (mySize == 0) {
		myHead = newNode;
		myTail = newNode;
	}
	else {
		myTail->next = newNode;
		myTail = newNode;
	}
	mySize++;
}

//print the list
void LinkedList::printList() {
	cout<<endl << "List" << endl;
	cout << "Item No\tItem Name" << endl;
	Node * pos = myHead;
	for (int i = 0; i < mySize; i++) {
		cout << pos->itemNo << "\t" << pos->itemName << endl;
		pos = pos->next;
	}
	cout << endl;
}

//remove a node from the begin of list
bool LinkedList::removeFromStart() {
	if (mySize == 0) {
		cout << "Sorry! The list is empty!";
		return false;
	}
	else if (mySize == 1) {
		myHead = NULL;
		myTail = NULL;
		mySize = 0;
	}
	else {
		Node * temp = myHead;
		myHead = temp->next;
		delete temp;
		mySize--;
		return true;
	}
}

//remove a node from the end of list
bool LinkedList::removeFromEnd() {
	if (mySize == 0) {
		cout << "Sorry! The list is empty!" << endl;
		return false;
	}
	else if (mySize == 1) {
		myHead = NULL;
		myTail = NULL;
		mySize = 0;
	}
	else {
		Node * temp = myHead;
		while (temp->next != myTail) {
			temp = temp->next;
		}
		myTail = temp;
		temp = temp=temp->next;
		myTail->next = NULL;
		delete temp;
		mySize--;
		return true;

	}
}

//delete a node by number
void LinkedList::removeNodeFromList(int num) {
	if (mySize == 0) {
		cout << "Sorry! The list is empty!" << endl;
	}
	else if (num==myHead->itemNo) {
		removeFromStart();
	}
	else if (num == myTail->itemNo) {
		removeFromEnd();
	}
	else {
		Node * cur = myHead;
		for (; cur->next != myTail; cur = cur->next) {
			if (cur->next->itemNo == num) {
				break;
			}
		}
		if (cur->next == myTail) {
			cout << "Error! Wrong number!" << endl;
		}
		else {
			Node *temp = cur->next;
			cur->next = temp->next;
			delete temp;
			mySize--;
		}
	}
}

//delete a node by name
void LinkedList::removeNodeFromList(string name) {
	if (mySize == 0) {
		cout << "Sorry! The list is empty!" << endl;
	}
	else if (name == myHead->itemName) {
		removeFromStart();
	}
	else if (name == myTail->itemName) {
		removeFromEnd();
	}
	else {
		Node * cur = myHead;
		for (; cur->next != myTail; cur = cur->next) {
			if (cur->next->itemName == name) {
				break;
			}
		}
		if (cur->next == myTail) {
			cout << "Error! Wrong name!" << endl;
		}
		else {
			Node *temp = cur->next;
			cur->next = temp->next;
			delete temp;
			mySize--;
		}
	}
}
//deconstructor
LinkedList::~LinkedList()
{
	myHead = NULL;
	myTail = NULL;
	mySize = 0;
}
