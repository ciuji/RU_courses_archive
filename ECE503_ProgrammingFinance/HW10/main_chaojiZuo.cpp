/*
Title: Homework 10. shopping list(linked list)

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time: Nov-14-2018

Course:332:503 Programming Finance
**/

#include <iostream>
#include "LinkedList.h"
using namespace std;

int printMenu();

int main()
{
	cout << "Welcome to the shopping list program" << endl;
	int choice = 0;
	//instance of the LinkedList
	LinkedList list;
	string itemName = "";
	int itemNum = -1;
	while (choice != 8) {
		choice = printMenu();
		switch (choice) {
		//insert at the begin of list
		case 1: {
			cout << "Please enter product number to insert at the begining:" << endl;
			cin >> itemNum;
			//judge wheather the user input the right number
			if (itemNum == 0) {
				cout << "Wrong input type!" << endl;
				break;
			}
			cout << "Please enter the name for the product：" << endl;
			cin >> itemName;
			cin.clear();
			cin.ignore(1024, '\n');
			Node * itemNode = new Node(itemName, itemNum);
			list.addToStart(itemNode);
			list.printList();
			break;
		}
		//insert at the end of list
		case 2: {
			cout << "Please enter product number to insert at the end:" << endl;
			cin >> itemNum;
			//judge weather the user input the right number.
			if (itemNum == 0) {
				cout << "Wrong input type!" << endl;
				break;
			}
			cout << "Please enter the name for the product：" << endl;
			cin >> itemName;
			cin.clear();
			cin.ignore(1024, '\n');
			Node * itemNode = new Node(itemName, itemNum);
			list.addToEnd(itemNode);
			list.printList();
			break;
		}
		//delete the first one
		case 3: {
			list.removeFromStart();
			list.printList();
			break;
		}
		//delete the last one
		case 4: {
			list.removeFromEnd();
			list.printList();
			break;
		}
		//call the function of delete by number
		case 5: {
			int delItem;
			cout << "Please enter the number for the product to delete:" << endl;
			cin >> delItem;
			cin.clear();
			cin.ignore(1024, '\n');
			list.removeNodeFromList(delItem);
			list.printList();
			break;
		}
		//call the function of delete by name.
		case 6: {
			string delItem;
			cout << "Please enter the name for the product to delete:" << endl;
			cin >> delItem;
			cin.clear();
			cin.ignore(1024, '\n');
			list.removeNodeFromList(delItem);
			list.printList();
			break;
		}
		//print the list.
		case 7: {
			list.printList();
			break;
		}
		//leave the loop.
		case 8:break;
		default: {
			cout << "Sorry! Wrong choice!" << endl;
			break;
		}
		}
	}
	system("pause");
	return 0;

}
//print menu function
int printMenu() {
	int choice = 0;
	cout << "Please choose an option" << endl;
	cout << "1. Add a new node at the beginning" << endl;
	cout << "2. Add a new node at the end" << endl;
	cout << "3. Remove the beginning node" << endl;
	cout << "4. Remove the end node" << endl;
	cout << "5. Remove a node from the list by entering an item number" << endl;
	cout << "6. Remove a node from the list by entering an item name" << endl;
	cout << "7. Print out the list" << endl;
	cout << "8. Quit the program" << endl;
	cin >> choice;
	cin.clear();
	cin.ignore(1024, '\n');
	return choice;

}
