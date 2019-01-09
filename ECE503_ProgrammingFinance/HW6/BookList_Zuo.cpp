#include "BookList_Zuo.h"
#include <iostream>
using namespace std;


BookList::BookList()
{
	for (int i = 0; i < MAXIMUN;i++){
		bookArr[i] = 0;
	}
	arrLen = 0;
	sorted = false;
}

//show menu
int BookList::menuFunc() {
	int choice = 0;
	cout << "What would you like to do?" << endl;
	cout << "\t1. Add an book to the end of the list" << endl;
	cout << "\t2. Add an book at a position" << endl;
	cout << "\t3. Find a book by ISBN number (linear search)" << endl;
	cout << "\t4. Find a book by ISBN number (binary search)" << endl;
	cout << "\t5. Delete a book at a position" << endl;
	cout << "\t6. Delete a book by ISBN number" << endl;
	cout << "\t7. Sort the list (using selection sort)" << endl;
	cout << "\t8. Sort the list (using bubble sort)" << endl;
	cout << "\t9. Print the list" << endl;
	cout << "\t0. Exit" << endl;
	cout << "your choice --- " << endl;
	cin >> choice;
	cin.clear();
	return choice;
}

//insert the new book at the end of the list.
void BookList::insert(int book) {
	insert_at(arrLen + 1, book);
}

//insert the new book at special position.
void BookList::insert_at(int position, int book) {
	if (arrLen < MAXIMUN) {
		if (position >= 1 && position <= (arrLen) + 1) {
			for (int i = arrLen; i >= position; i--) {
				*(bookArr + i) = *(bookArr + i - 1);
			}
			arrLen += 1;
			*(bookArr + position - 1) = book;
			print();
			sorted = false;
		}
		else {
			cout << "Error: Wrong position!" << endl;
		}
	}
	else {
		cout << "Error: You can not buy more than 20 books" << endl;
	}
}

//use linear search to find a book.
int BookList::find_linear(int book) const {
	//use result to store the position.
	int result = 0;
	for (int i = 0; i < arrLen; i++) {
		if (*(bookArr + i) == book) {
			result = i + 1;
			break;
		}
	}
	if (result) {
		cout << "The book you search is in position " << result << endl;
	}
	else {
		cout << "Sorry, Book not found" << endl;

	}
	return result;
}

//use binary search to find a book.
int BookList::find_binary(int book) const {
	//use result to store the position.
	int result = 0;
	if (sorted) {
		//initial the parameters. hp is the high position, lp is the low position.
		int lp = 0, hp = arrLen - 1;
		int mp = (lp + hp) / 2;
		//do the binary search.
		while (lp <= hp) {
			if (book == *(bookArr + mp)) {
				result = mp + 1;
				break;
			}
			else {
				if (book > *(bookArr + mp)) {
					lp = mp + 1;
					mp = (lp + hp) / 2;
				}
				else
				{
					hp = mp - 1;
					mp = (hp + lp) / 2;
				}
			}
		}
	}

	if (result) {
		cout << "The book your search is in position " << result << endl;
	}
	else {
		cout << "Sorry, book not found" << endl;
	}
	return result;
}

//delete a book by position
void BookList::delete_item_position(int position) {
	if (position >= 1 && position <= arrLen) {
		//move the element in list
		for (int i = position; i < arrLen; i++) {
			*(bookArr + i - 1) = *(bookArr + i);
		}
		arrLen -= 1;
		print();
	}
	else {
		cout << "Error: Wrong position!" << endl;
	}
}
//use book's ISBN to delete
void BookList::delete_item_isbn( int element) {
	//find the position of the book.
	int position = 0;
	for (int i = 0; i < arrLen; i++) {
		if (*(bookArr + i) == element) {
			position = i + 1;
			break;
		}
	}
	if (!position) {
		cout << "Sorry, Book not found" << endl;

	}
	else
		delete_item_position( position);
}
//find the book by selection sort
void BookList::sort_list_selection() {
	//selection sort
	int temp = 0;
	for (int i = 0; i < arrLen - 1; i++)
	{
		int min_pos = i;
		for (int j = i; j < arrLen; j++)
		{
			if (*(bookArr + j) < *(bookArr + min_pos))
			{
				min_pos = j;
			}
		}
		temp = *(bookArr + min_pos);
		*(bookArr + min_pos) = *(bookArr + i);
		*(bookArr + i) = temp;
	}


	cout << "Selection sort successfully!" << endl;
	sorted = 1;
	print();
}

void BookList::sort_list_bubble() {
	int temp = 0;
	//do the bubble.
	for (int i = 0; i < arrLen - 1; i++) {
		for (int j = 0; j < arrLen - i - 1; j++) {
			if (*(bookArr + j) > *(bookArr + j + 1)) {
				temp = *(bookArr + j);
				*(bookArr + j) = *(bookArr + j + 1);
				*(bookArr + j + 1) = temp;
			}
		}
	}
	cout << "Bubble sort successfully!" << endl;
	sorted = 1;
	print();
}

void BookList::print() {
	cout << "Your list is now:" << endl;
	//if their is no book in the list.
	if (!arrLen) {
		cout << "No book" << endl;
	}
	else {
		for (int i = 0; i < arrLen; i++) {
			cout << i + 1 << ". " << *(bookArr + i) << endl;
		}
		cout << endl;
	}
}

bool BookList::getIfSort() {
	return sorted;
}

BookList::~BookList()
{
}
