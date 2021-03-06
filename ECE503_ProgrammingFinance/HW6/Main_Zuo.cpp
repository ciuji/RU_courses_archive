/*
Title: Homework 6 Booklist Class

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time: Oct-17-2018

Course:332:503 Programming Finance
**/
//Booklist class


#include <iostream>
#include "BookList_Zuo.h"
using namespace std;

int main() {
	BookList myList;

	int choice=myList.menuFunc();
	int position = 0, item = 0;
	while (choice != 0) {
		//get the ISBN of book
		if (choice == 1 || choice == 2 || choice == 3 || choice == 6) {
			cout << "Please type in the element" << endl;
			cin >> item;
		}
		//get the position
		if (choice == 2 || choice == 5) {
			cout << "At what position?" << endl;
			cin >> position;
		}
		//judge can whether the user use call the find_binary function.
		if (choice == 4) {
			if (myList.getIfSort()) {
				cout << "Please type in the element" << endl;
				cin >> item;
			}
			else {
				cout << "Sorry, your have to sort the list before binary search." << endl;
			}
		}
		//switch to call different function.
		switch (choice) {
		case 1: myList.insert(item); break;
		case 2: myList.insert_at(position,item); break;
		case 3: myList.find_linear( item); break;
		case 4: {
			if (myList.getIfSort())
				myList.find_binary(item);
		}break;
		case 5: myList.delete_item_position( position); break;
		case 6: myList.delete_item_isbn(item); break;
		case 7: myList.sort_list_selection( ); break;
		case 8: myList.sort_list_bubble( ); break;
		case 9: myList.print(); break;
		case 0: choice = 0; break;
		default: cout << "Not supported!" << endl; break;
		}
		choice = myList.menuFunc();
	}
	system("pause");
	return 0;
}