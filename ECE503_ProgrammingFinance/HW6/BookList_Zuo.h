/*
Title: Homework 6 Booklist Class

Author: Chaoji Zuo

Email: chaoji.zuo@rutgers.edu

Time: Oct-17-2018

Course:332:503 Programming Finance
**/
//Booklist class
#ifndef BOOKLIST_H

#define BOOKLIST_H
#define MAXIMUN 20
#include <iostream>

class BookList {
public:
	BookList();
	int menuFunc();
	void insert(int book);
	void insert_at(int position, int book);
	int find_linear(int book) const;
	int find_binary(int book) const;
	void delete_item_position(int position);
	void delete_item_isbn(int book);
	void sort_list_selection();
	void sort_list_bubble();
	void print();
	//use getIfSort to get private member sorted.
	bool getIfSort();

	~BookList();
private:
	int bookArr[MAXIMUN];
	int arrLen;
	bool sorted;
};

#endif